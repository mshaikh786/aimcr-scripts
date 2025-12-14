#!/usr/bin/env python3
"""
Simple WSI Viewer using OpenSlide
Usage: python view_wsi.py <slide.svs> [options]
       python view_wsi.py --batch <input_folder> --output-dir <output_folder>
"""

import sys
import os
import argparse
from pathlib import Path
from openslide import OpenSlide
import matplotlib.pyplot as plt

def view_wsi(slide_path, thumbnail_size=(2000, 2000), show_region=False, 
             region_x=None, region_y=None, region_size=2048, save_output=None):
    """
    View a whole slide image
    
    Args:
        slide_path: Path to the SVS file
        thumbnail_size: Size of thumbnail to generate
        show_region: Whether to show a high-resolution region
        region_x: X coordinate for region (None = center)
        region_y: Y coordinate for region (None = center)
        region_size: Size of region to extract
        save_output: Path to save output image (None = just display)
    """
    
    try:
        # Open slide
        print(f"Opening: {slide_path}")
        slide = OpenSlide(slide_path)
        
        # Print information
        print("\n" + "="*70)
        print("Slide Information:")
        print("="*70)
        print(f"Dimensions: {slide.dimensions[0]:,} x {slide.dimensions[1]:,} pixels")
        print(f"Resolution levels: {slide.level_count}")
        
        for i, dim in enumerate(slide.level_dimensions):
            downsample = slide.level_downsamples[i]
            print(f"  Level {i}: {dim[0]:,} x {dim[1]:,} pixels (downsample: {downsample:.1f}x)")
        
        # Check for magnification
        if 'aperio.AppMag' in slide.properties:
            print(f"Magnification: {slide.properties['aperio.AppMag']}x")
        
        if 'aperio.MPP' in slide.properties:
            print(f"Microns per pixel: {slide.properties['aperio.MPP']}")
        
        print("="*70 + "\n")
        
        # Create figure
        if show_region:
            fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        else:
            fig, axes = plt.subplots(1, 1, figsize=(15, 15))
            axes = [axes]
        
        # Get and display thumbnail
        print("Creating thumbnail...")
        thumbnail = slide.get_thumbnail(thumbnail_size)
        axes[0].imshow(thumbnail)
        axes[0].axis('off')
        axes[0].set_title(f'Full Slide: {slide_path.split("/")[-1]}\n'
                         f'Dimensions: {slide.dimensions[0]:,} x {slide.dimensions[1]:,}',
                         fontsize=12)
        
        # Show high-resolution region if requested
        if show_region:
            print("Extracting high-resolution region...")
            
            # Default to center if coordinates not provided
            if region_x is None:
                region_x = slide.dimensions[0] // 2 - region_size // 2
            if region_y is None:
                region_y = slide.dimensions[1] // 2 - region_size // 2
            
            # Ensure coordinates are within bounds
            region_x = max(0, min(region_x, slide.dimensions[0] - region_size))
            region_y = max(0, min(region_y, slide.dimensions[1] - region_size))
            
            # Read region at highest resolution
            region = slide.read_region(
                (region_x, region_y),
                0,
                (region_size, region_size)
            )
            region = region.convert('RGB')
            
            axes[1].imshow(region)
            axes[1].axis('off')
            axes[1].set_title(f'High Resolution Region\n'
                             f'Location: ({region_x:,}, {region_y:,}), '
                             f'Size: {region_size}x{region_size}',
                             fontsize=12)
        
        plt.tight_layout()
        
        # Save or show
        if save_output:
            plt.savefig(save_output, dpi=150, bbox_inches='tight')
            print(f"Saved to: {save_output}")
        else:
            plt.show()
        
        plt.close()
        slide.close()
        print("\nDone!")
        
    except FileNotFoundError:
        print(f"Error: File not found: {slide_path}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


def batch_process_slides(input_folder, output_folder=None, thumbnail_size=(2000, 2000),
                         show_region=False, region_x=None, region_y=None, 
                         region_size=2048, file_extension='.svs'):
    """
    Process all WSI files in a folder and save them as PNG
    
    Args:
        input_folder: Folder containing SVS files
        output_folder: Folder to save PNG files (default: input_folder/output)
        thumbnail_size: Size of thumbnail
        show_region: Whether to show high-resolution region
        region_x: X coordinate for region
        region_y: Y coordinate for region
        region_size: Size of region to extract
        file_extension: File extension to search for (e.g., '.svs', '.tif')
    """
    
    # Validate input folder
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder not found: {input_folder}")
        return 1
    
    # Set default output folder
    if output_folder is None:
        output_folder = os.path.join(input_folder, 'output')
    
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)
    
    # Find all SVS files
    input_path = Path(input_folder)
    slide_files = list(input_path.glob(f'*{file_extension}'))
    
    if not slide_files:
        print(f"No {file_extension} files found in {input_folder}")
        return 1
    
    print("="*70)
    print(f"Batch Processing WSI Files")
    print("="*70)
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print(f"Found {len(slide_files)} {file_extension} file(s)")
    print(f"Thumbnail size: {thumbnail_size[0]} x {thumbnail_size[1]}")
    if show_region:
        print(f"Region size: {region_size} x {region_size}")
    print("="*70)
    print()
    
    # Process each file
    successful = 0
    failed = 0
    
    for i, slide_path in enumerate(slide_files, 1):
        slide_name = slide_path.name
        output_name = slide_path.stem + '.png'
        output_path = os.path.join(output_folder, output_name)
        
        print(f"[{i}/{len(slide_files)}] Processing: {slide_name}")
        
        # Skip if output already exists
        if os.path.exists(output_path):
            print(f"  Output already exists, skipping: {output_name}")
            successful += 1
            print()
            continue
        
        # Process the slide
        try:
            result = view_wsi(
                slide_path=str(slide_path),
                thumbnail_size=thumbnail_size,
                show_region=show_region,
                region_x=region_x,
                region_y=region_y,
                region_size=region_size,
                save_output=output_path
            )
            
            if result == 0:
                successful += 1
                print(f"  ✓ Saved: {output_name}")
            else:
                failed += 1
                print(f"  ✗ Failed: {slide_name}")
        except Exception as e:
            failed += 1
            print(f"  ✗ Error processing {slide_name}: {e}")
        
        print()
    
    # Summary
    print("="*70)
    print("Batch Processing Summary")
    print("="*70)
    print(f"Total files: {len(slide_files)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Output folder: {os.path.abspath(output_folder)}")
    print("="*70)
    
    return 0 if failed == 0 else 1


def main():
    parser = argparse.ArgumentParser(
        description='View TCGA Whole Slide Images (SVS format) using OpenSlide',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # View a single slide (shows thumbnail)
  python view_wsi.py TCGA-XX-XXXX-01A-01-DX1.svs

  # View thumbnail and high-resolution region from center
  python view_wsi.py TCGA-XX-XXXX-01A-01-DX1.svs --region

  # View specific region at coordinates
  python view_wsi.py TCGA-XX-XXXX-01A-01-DX1.svs --region --x 10000 --y 20000

  # Save output instead of displaying
  python view_wsi.py TCGA-XX-XXXX-01A-01-DX1.svs --region --output slide_view.png

  # Batch process: Convert all SVS files in a folder to PNG
  python view_wsi.py --batch input_folder/ --output-dir output_pngs/

  # Batch process with regions
  python view_wsi.py --batch input_folder/ --output-dir output_pngs/ --region

  # Custom thumbnail and region size
  python view_wsi.py TCGA-XX-XXXX-01A-01-DX1.svs --region --thumb-size 3000 --region-size 4096
        """
    )
    
    parser.add_argument('filename', nargs='?', default=None,
                        help='Path to the SVS slide file (not needed with --batch)')
    
    parser.add_argument('--batch', type=str, default=None,
                        help='Process all SVS files in the specified folder')
    
    parser.add_argument('--output-dir', type=str, default=None,
                        help='Output directory for batch processing or single file save location')
    
    parser.add_argument('--region', action='store_true',
                        help='Show a high-resolution region alongside thumbnail')
    
    parser.add_argument('--x', type=int, default=None,
                        help='X coordinate for region (default: center)')
    
    parser.add_argument('--y', type=int, default=None,
                        help='Y coordinate for region (default: center)')
    
    parser.add_argument('--region-size', type=int, default=2048,
                        help='Size of region to extract (default: 2048)')
    
    parser.add_argument('--thumb-size', type=int, default=2000,
                        help='Size of thumbnail (default: 2000)')
    
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Save output to file instead of displaying (for single file mode)')
    
    parser.add_argument('--ext', type=str, default='.svs',
                        help='File extension to search for in batch mode (default: .svs)')
    
    args = parser.parse_args()
    
    # Batch processing mode
    if args.batch:
        return batch_process_slides(
            input_folder=args.batch,
            output_folder=args.output_dir,
            thumbnail_size=(args.thumb_size, args.thumb_size),
            show_region=args.region,
            region_x=args.x,
            region_y=args.y,
            region_size=args.region_size,
            file_extension=args.ext
        )
    
    # Single file mode
    if not args.filename:
        parser.print_help()
        print("\nError: Either provide a filename or use --batch mode")
        return 1
    
    # Determine output path
    output_path = args.output
    if args.output_dir and not args.output:
        # If output-dir is specified, save there
        os.makedirs(args.output_dir, exist_ok=True)
        basename = Path(args.filename).stem
        output_path = os.path.join(args.output_dir, f"{basename}.png")
    
    # Call viewer
    return view_wsi(
        slide_path=args.filename,
        thumbnail_size=(args.thumb_size, args.thumb_size),
        show_region=args.region,
        region_x=args.x,
        region_y=args.y,
        region_size=args.region_size,
        save_output=output_path
    )


if __name__ == "__main__":
    sys.exit(main())
