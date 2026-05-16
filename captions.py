# ============================================================
# Install required packages
# ============================================================
!pip install transformers torch torchvision pillow tqdm --quiet

# ============================================================
# Imports
# ============================================================
import os
import json
from tqdm import tqdm
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration

# ============================================================
# Configuration
# ============================================================
BASE_DIR = "/kaggle/input/6-modern-urban"  # dataset path
CAPTION_DIR = "/kaggle/working/architecture_captions"
os.makedirs(CAPTION_DIR, exist_ok=True)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", DEVICE)

# ============================================================
# Load BLIP-2
# ============================================================
print("Loading BLIP-2 model...")
processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xl")
model.to(DEVICE)

# ============================================================
# Helper function
# ============================================================
def generate_blip_caption(image_path):
    """Generate caption using BLIP-2"""
    try:
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        prompt = f"Describe this architectural image '{image_name}' in detail, including roof type, materials, style, colors, lighting, and setting."

        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, text=prompt, return_tensors="pt").to(DEVICE)
        out = model.generate(**inputs, max_new_tokens=80)
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        print(f"Error on {image_path}: {e}")
        return None

# ============================================================
# Main loop: process all images directly under BASE_DIR
# ============================================================
images = [f for f in os.listdir(BASE_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
captions_out = {}

print(f"Found {len(images)} images directly under {BASE_DIR}")

for img_name in tqdm(images):
    img_path = os.path.join(BASE_DIR, img_name)
    caption = generate_blip_caption(img_path)
    if caption:
        captions_out[img_name] = caption

# Save all captions in one JSON
out_file = os.path.join(CAPTION_DIR, "all_captions.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(captions_out, f, indent=4, ensure_ascii=False)

print("\n✅ Captions generated and saved in", out_file)
