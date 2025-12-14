#!/usr/bin/env python3
"""
Script to download 30 random datasets from TCGA program via GDC API
"""

import requests
import json
import random
import os
import sys
from pathlib import Path

# Configuration
GDC_API_BASE = "https://api.gdc.cancer.gov"
FILES_ENDPOINT = f"{GDC_API_BASE}/files"
DATA_ENDPOINT = f"{GDC_API_BASE}/data"
DOWNLOAD_DIR = "tcga_downloads"
NUM_DATASETS = 30

def query_tcga_files(data_type=None, experimental_strategy=None, max_results=1000):
    """
    Query GDC API for TCGA files
    
    Args:
        data_type: Type of data (e.g., 'Gene Expression Quantification')
        experimental_strategy: e.g., 'RNA-Seq', 'WXS', etc.
        max_results: Maximum number of results to retrieve
    
    Returns:
        List of file metadata dictionaries
    """
    filters = {
        "op": "and",
        "content": [
            {
                "op": "in",
                "content": {
                    "field": "cases.project.program.name",
                    "value": ["TCGA"]
                }
            },
            {
                "op": "=",
                "content": {
                    "field": "access",
                    "value": "open"
                }
            }
        ]
    }
    
    # Add optional filters
    if data_type:
        filters["content"].append({
            "op": "=",
            "content": {
                "field": "data_type",
                "value": data_type
            }
        })
    
    if experimental_strategy:
        filters["content"].append({
            "op": "=",
            "content": {
                "field": "experimental_strategy",
                "value": experimental_strategy
            }
        })
    
    params = {
        "filters": json.dumps(filters),
        "format": "JSON",
        "fields": "file_id,file_name,file_size,data_type,experimental_strategy,cases.project.project_id",
        "size": max_results
    }
    
    print(f"Querying GDC API for TCGA files...")
    response = requests.get(FILES_ENDPOINT, params=params)
    
    if response.status_code != 200:
        print(f"Error querying API: {response.status_code}")
        print(response.text)
        return []
    
    data = response.json()
    files = data.get("data", {}).get("hits", [])
    
    print(f"Found {len(files)} files matching criteria")
    return files


def download_file(file_id, file_name, output_dir):
    """
    Download a single file from GDC
    
    Args:
        file_id: UUID of the file
        file_name: Name to save the file as
        output_dir: Directory to save the file
    
    Returns:
        True if successful, False otherwise
    """
    url = f"{DATA_ENDPOINT}/{file_id}"
    output_path = os.path.join(output_dir, file_name)
    
    # Skip if already downloaded
    if os.path.exists(output_path):
        print(f"  File already exists: {file_name}")
        return True
    
    print(f"  Downloading: {file_name}")
    
    try:
        response = requests.get(url, stream=True)
        
        if response.status_code != 200:
            print(f"    Error downloading file: {response.status_code}")
            return False
        
        # Get file size from headers
        total_size = int(response.headers.get('content-length', 0))
        
        with open(output_path, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # Simple progress indicator
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r    Progress: {progress:.1f}%", end='', flush=True)
        
        print()  # New line after progress
        print(f"    Downloaded: {file_name} ({total_size / (1024*1024):.2f} MB)")
        return True
        
    except Exception as e:
        print(f"    Error downloading {file_name}: {str(e)}")
        if os.path.exists(output_path):
            os.remove(output_path)
        return False


def main():
    """Main function to orchestrate the download process"""
    
    # Parse command line arguments for customization
    import argparse
    parser = argparse.ArgumentParser(description='Download random TCGA datasets from GDC')
    parser.add_argument('--num', type=int, default=NUM_DATASETS,
                        help=f'Number of datasets to download (default: {NUM_DATASETS})')
    parser.add_argument('--data-type', type=str, default=None,
                        help='Filter by data type (e.g., "Gene Expression Quantification")')
    parser.add_argument('--strategy', type=str, default=None,
                        help='Filter by experimental strategy (e.g., "RNA-Seq")')
    parser.add_argument('--output-dir', type=str, default=DOWNLOAD_DIR,
                        help=f'Output directory (default: {DOWNLOAD_DIR})')
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed for reproducibility')
    
    args = parser.parse_args()
    
    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        print(f"Using random seed: {args.seed}")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    print(f"Output directory: {args.output_dir}\n")
    
    # Query for files
    files = query_tcga_files(
        data_type=args.data_type,
        experimental_strategy=args.strategy
    )
    
    if not files:
        print("No files found matching criteria!")
        return 1
    
    # Randomly select files
    num_to_download = min(args.num, len(files))
    selected_files = random.sample(files, num_to_download)
    
    print(f"\nRandomly selected {num_to_download} files for download\n")
    
    # Display selection summary
    print("=" * 80)
    print("Selected Files:")
    print("=" * 80)
    for i, file_info in enumerate(selected_files, 1):
        file_id = file_info['file_id']
        file_name = file_info['file_name']
        file_size = file_info.get('file_size', 0) / (1024 * 1024)  # Convert to MB
        data_type = file_info.get('data_type', 'N/A')
        project = file_info.get('cases', [{}])[0].get('project', {}).get('project_id', 'N/A') if file_info.get('cases') else 'N/A'
        
        print(f"{i:2d}. {file_name}")
        print(f"    ID: {file_id}")
        print(f"    Size: {file_size:.2f} MB")
        print(f"    Type: {data_type}")
        print(f"    Project: {project}")
        print()
    
    print("=" * 80)
    print(f"\nStarting downloads...\n")
    
    # Download files
    successful = 0
    failed = 0
    
    for i, file_info in enumerate(selected_files, 1):
        file_id = file_info['file_id']
        file_name = file_info['file_name']
        
        print(f"[{i}/{num_to_download}] File: {file_name}")
        
        if download_file(file_id, file_name, args.output_dir):
            successful += 1
        else:
            failed += 1
        
        print()
    
    # Summary
    print("=" * 80)
    print("Download Summary:")
    print("=" * 80)
    print(f"Total files selected: {num_to_download}")
    print(f"Successfully downloaded: {successful}")
    print(f"Failed: {failed}")
    print(f"Output directory: {os.path.abspath(args.output_dir)}")
    print("=" * 80)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
