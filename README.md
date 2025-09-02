# COCO Image Captioning Project
## Overview
This project demonstrates image captioning using the COCO 2017 dataset. It provides tools to prepare the dataset, load images with their corresponding captions, and visualize samples for analysis or model development.

## Dataset Information
**COCO (Common Objects in Context)** is a large-scale dataset containing:
- 5,000 validation images
- Multiple human-written captions per image (typically 5 captions each)
- Object detection annotations and segmentation masks
- High-quality, diverse real-world scenes

## Project Structure
```
project/
├── README.md
├── annotations_trainval2017.zip          # Provided annotations
├── step1_prepare_data.py                 # Data preparation script
├── step2_load_and_visualize.py          # Dataset loading & visualization
└── data/coco/                           # Generated after Step 1
    ├── annotations/
    │   ├── captions_train2017.json
    │   ├── captions_val2017.json
    │   └── instances_val2017.json
    └── images/
        └── val2017/                     # 5,000 validation images
            ├── 000000000139.jpg
            ├── 000000000285.jpg
            └── ...
```

## System Requirements
- **Python**: 3.7 or higher
- **Disk Space**: ~1GB for validation images
- **Internet**: Required for initial image download
- **Memory**: ~2GB RAM recommended for dataset loading

## Installation
```bash
pip install torchvision pycocotools matplotlib pillow tqdm
```

## Usage Guide

### Step 1: Data Preparation
Extracts annotations and downloads validation images:
```bash
python step1_prepare_data.py
```

**What it does:**
- Extracts JSON files from `annotations_trainval2017.zip`
- Downloads COCO val2017 images (~1GB)
- Organizes files into proper directory structure

**Expected output:**
```
✅ Extracted Annotations: ['captions_train2017.json', 'captions_val2017.json', ...]
⬇️ Downloading val2017 images...
✅ Extracted Images: 5000
```

### Step 2: Dataset Loading & Visualization
Loads the prepared dataset and displays a sample:
```bash
python step2_load_and_visualize.py
```

**What it does:**
- Creates PyTorch dataset from prepared files
- Loads image-caption pairs
- Displays sample image with all associated captions

**Expected output:**
```
✅ Total validation samples: 5000
📜 Captions:
- A man riding a bike down a street.
- A cyclist with a helmet on a road.
...
```

## File Paths Configuration
```python
DATA_DIR = Path("data/coco")
IMG_DIR = DATA_DIR / "images"
VAL_DIR = IMG_DIR / "val2017"
ANN_DIR = DATA_DIR / "annotations"
ANNOTATIONS_ZIP = Path("annotations_trainval2017.zip")
```

