Step 1:
Download random 30 images from TCGA project:
python download.py --num 30 --data-type "Slide Image"

Step 2: 
Convert all or some to PNG for visual inspection
python view_wsi.py --batch tcga_downloads --output-dir tcga_downloads_png
