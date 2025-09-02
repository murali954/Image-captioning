
import zipfile
from pathlib import Path
import requests

DATA_DIR = Path("data/coco")
IMG_DIR = DATA_DIR / "images"
VAL_DIR = IMG_DIR / "val2017"
ANN_DIR = DATA_DIR / "annotations"

ANNOTATIONS_ZIP = Path("annotations_trainval2017.zip")  # already uploaded

# Create dirs
for p in [IMG_DIR, VAL_DIR, ANN_DIR]:
    p.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(ANNOTATIONS_ZIP, "r") as zip_ref:
    zip_ref.extractall(ANN_DIR)

print("✅ Extracted Annotations:", [f.name for f in ANN_DIR.glob("*.json")])

# 2. Download Validation Images (~1GB)
url = "http://images.cocodataset.org/zips/val2017.zip"
zip_path = IMG_DIR / "val2017.zip"

if not zip_path.exists():
    print("⬇️ Downloading val2017 images...")
    r = requests.get(url, stream=True)
    with open(zip_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            f.write(chunk)
    print("✅ Download complete.")

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(IMG_DIR)

print("✅ Extracted Images:", len(list(VAL_DIR.glob("*.jpg"))))
