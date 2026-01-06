from pathlib import Path
import pandas as pd
from loguru import logger

# Paths setup
BASE_DIR = Path(__file__).resolve().parents[1]
BRONZE_DIR = BASE_DIR / "data" / "bronze"
SILVER_DIR = BASE_DIR / "data" / "silver"

RAW_FILE_NAME = "bank_customer_churn_raw.csv"
RAW_FILE_PATH = BRONZE_DIR / RAW_FILE_NAME
SILVER_FILE_PATH = SILVER_DIR / "bank_customer_churn_clean.parquet"

def clean_data():
    logger.info("Starting data cleaning (Silver layer)")
    
    # Load raw data
    df = pd.read_csv(RAW_FILE_PATH)
    
    # Drop non-analytical columns (Corrected 'columns' spelling)
    df = df.drop(columns=["RowNumber", "Surname"])
    logger.info("Dropped non-analytical columns")
    
    # Check for duplicates (Corrected 'CustomerId' spelling)
    if df["CustomerId"].duplicated().any():
        logger.warning('Duplicated CustomerId found')
    else:
        logger.info("CustomerId is unique")
    
    # Standardize column names (Lower case and stripped)
    df.columns = (
        df.columns 
        .str.strip()
        .str.lower()
    )
    
    # Optimize data types for flags
    flag_columns = ["hascrcard", "isactivemember", "exited"]
    for col in flag_columns:
        if col in df.columns:
            df[col] = df[col].astype("int8")
            
    # Save to Silver Layer in Parquet format
    SILVER_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(SILVER_FILE_PATH, index=False)
    
    logger.info(f"Silver dataset saved at {SILVER_FILE_PATH}")
    return df

if __name__ == "__main__":
    clean_data()