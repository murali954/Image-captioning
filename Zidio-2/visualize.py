

from pathlib import Path
import matplotlib.pyplot as plt
import torchvision.transforms as T
from torchvision.datasets import CocoCaptions
from PIL import Image

DATA_DIR = Path("data/coco")
VAL_DIR = DATA_DIR / "images" / "val2017"
ANN_DIR = DATA_DIR / "annotations"

transform = T.Compose([
    T.Resize((256, 256)),
    T.ToTensor()
])

coco_val = CocoCaptions(
    root=str(VAL_DIR),
    annFile=str(ANN_DIR / "captions_val2017.json"),
    transform=transform
)

print("✅ Total validation samples:", len(coco_val))

img, captions = coco_val[0]
plt.imshow(img.permute(1, 2, 0))
plt.axis("off")
plt.title("Sample COCO Image")
plt.show()

print("📜 Captions:")
for c in captions:
    print("-", c)
