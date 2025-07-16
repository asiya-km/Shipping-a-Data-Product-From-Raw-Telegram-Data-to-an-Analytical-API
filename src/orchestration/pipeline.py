from dagster import job, op

@op
def scrape_telegram_data():
    # Call your scraping script here
    pass

@op
def load_raw_to_postgres():
    # Load raw JSON to Postgres
    pass

@op
def run_dbt_transformations():
    # Run dbt models
    pass

@op
def run_yolo_enrichment():
    # Run YOLO enrichment
    pass

@job
def telegram_pipeline():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment() 