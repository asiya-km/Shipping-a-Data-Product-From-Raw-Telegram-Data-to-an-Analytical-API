import os
from ultralytics import YOLO
from dotenv import load_dotenv
import json

load_dotenv()
YOLO_MODEL_PATH = os.getenv('YOLO_MODEL_PATH')

model = YOLO(YOLO_MODEL_PATH)

IMAGES_DIR = os.path.join(os.path.dirname(__file__), '../../data/raw/telegram_images')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '../../data/raw/image_detections.json')

def detect_on_images():
    results = []
    for root, _, files in os.walk(IMAGES_DIR):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, file)
                detections = model(img_path)
                for det in detections:
                    for box in det.boxes:
                        results.append({
                            'image_path': img_path,
                            'class': box.cls.item(),
                            'confidence': box.conf.item()
                        })
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == '__main__':
    detect_on_images() 