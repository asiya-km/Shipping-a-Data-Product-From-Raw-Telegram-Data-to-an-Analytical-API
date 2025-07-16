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
2. Build and start the stack:
   ```bash
   docker-compose up --build
   ```
3. Run scraping, enrichment, and API scripts as needed.

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