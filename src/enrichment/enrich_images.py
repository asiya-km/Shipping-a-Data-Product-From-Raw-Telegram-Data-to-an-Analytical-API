import os
from ultralytics import YOLO
from dotenv import load_dotenv
import json
from loguru import logger

load_dotenv()
YOLO_MODEL_PATH = os.getenv('YOLO_MODEL_PATH')

model = YOLO(YOLO_MODEL_PATH)

IMAGES_DIR = os.path.join(os.path.dirname(__file__), '../../data/raw/telegram_images')
MESSAGES_INDEX = os.path.join(os.path.dirname(__file__), '../../data/raw/image_message_index.json')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '../../data/raw/image_detections.json')
LOG_FILE = os.path.join(os.path.dirname(__file__), '../../data/enrich.log')

logger.add(LOG_FILE, rotation="1 MB")

def load_message_index():
    if os.path.exists(MESSAGES_INDEX):
        with open(MESSAGES_INDEX, 'r') as f:
            return json.load(f)
    return {}

def detect_on_images():
    results = []
    message_index = load_message_index()
    for root, _, files in os.walk(IMAGES_DIR):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, file)
                message_id = message_index.get(file)
                if not message_id:
                    logger.warning(f"No message_id found for image {file}")
                    continue
                try:
                    detections = model(img_path)
                    for det in detections:
                        for box in det.boxes:
                            results.append({
                                'message_id': message_id,
                                'detected_object_class': box.cls.item(),
                                'confidence_score': box.conf.item()
                            })
                except Exception as e:
                    logger.error(f"Error processing {img_path}: {e}")
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2)
    logger.info(f"Saved detections to {OUTPUT_FILE}")

if __name__ == '__main__':
    detect_on_images() 