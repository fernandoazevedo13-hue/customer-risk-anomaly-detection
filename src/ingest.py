from pathlib import Path
import pandas as pd
from loguru import logger

BASE_DIR = Path(__file__).resolve().parents[1]

BRONZE_DIR = BASE_DIR / "data" / "bronze"
RAW_FILE_NAME = "bank_customer_churn_raw.csv"

RAW_FILE_PATH = BRONZE_DIR / RAW_FILE_NAME


def ingest_data():
    logger.info("Staring data ingestion (Bronze Layer)")
    # Validation: Check if the raw file exists before proceeding
    if not RAW_FILE_PATH.exists():
        logger.error(f"Raw data file not found: {RAW_FILE_PATH}")
        raise FileNotFoundError(f"File nto found: {RAW_FILE_PATH}")
    df = pd.read_csv(RAW_FILE_PATH)
    # Audit logs: Documenting the dataset metadata
    logger.info("Raw dataset loaded successfully")
    logger.info(f"Dataset shape: {df.shape}")
    logger.info(f"Columns: {list(df.columns)}")
    logger.info("Data types:")
    logger.info(df.dtypes)

    return df


if __name__ == "__main__":
    ingest_data()

