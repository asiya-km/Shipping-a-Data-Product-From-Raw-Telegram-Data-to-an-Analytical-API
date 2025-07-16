# Shipping a Data Product: From Raw Telegram Data to an Analytical API

## Overview
This project is an end-to-end data pipeline for extracting, transforming, enriching, and serving insights from public Telegram channels about Ethiopian medical businesses. It uses Telethon for scraping, dbt for transformation, YOLOv8 for image enrichment, FastAPI for analytics, and Dagster for orchestration.

## Project Structure
```
Shipping a Data Product From Raw Telegram Data to an Analytical API/
├── data/
│   └── raw/telegram_messages/YYYY-MM-DD/channel_name.json
├── dbt/
├── src/
│   ├── scraping/
│   ├── enrichment/
│   │   └── models/  # Place YOLO model weights here
│   ├── api/
│   └── orchestration/
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
```

## Setup
1. Copy `.env.example` to `.env` and fill in your secrets.
2. Place YOLO model weights (e.g., `yolov8.pt`) in `src/enrichment/models/` and update `YOLO_MODEL_PATH` in your `.env`.
3. Build and start the stack:
   ```bash
   docker-compose up --build
   ```
4. Run scraping, enrichment, and API scripts as needed.
5. Develop your dbt models in the `dbt/` directory.

## External Files
- **YOLO Model Weights:** Place the contents of `yolo.zip` (e.g., `yolov8.pt`) in `src/enrichment/models/`.
- **YOLO Notebook:** `src/enrichment/models/Yolo.ipynb` is for demonstration and experimentation. It is not used in the production pipeline, but can be referenced for development or presentation.
- **Dagster Example Files:** Files like `pipeline_with_schedule.py` and `main.py` in `src/orchestration/` are examples (e.g., COVID ETL) and not part of the main Telegram pipeline. Your main pipeline is in `pipeline.py`.
- **Sample Images:** Place in `data/raw/telegram_images/` if provided.
- **Large files and models are not committed to the repository.** See `.gitignore` for details.

## Best Practices for Large Files
- Do not commit large model weights or sample data to GitHub.
- Use `.gitignore` to exclude these files and provide instructions for placement in the README.

## Main Components
- **Scraping:** Extracts Telegram messages and images to `data/raw/telegram_messages`.
- **dbt:** Transforms raw data into a star schema in PostgreSQL.
- **YOLOv8:** Enriches image data with object detection.
- **FastAPI:** Serves analytical endpoints.
- **Dagster:** Orchestrates the pipeline.

## Data Folders
- `data/raw/telegram_messages/YYYY-MM-DD/channel_name.json`: Raw Telegram data.
- Add `.gitkeep` to empty folders to track them in git.

## Development
- All code is in `src/`.
- Use `python-dotenv` for environment variables.

## License
MIT 