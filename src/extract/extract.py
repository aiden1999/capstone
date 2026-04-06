"""Extraction phase of the ETL process.

Called in run_etl.
"""

import polars as pl

from src.constants import (
    DISRUPTIONS_FILE,
    DISRUPTIONS_USECOLS,
    RAW_DATA_FILE_PATH,
    SERVICES_FILE,
    SERVICES_USECOLS,
    STATIONS_FILE,
    STATIONS_USECOLS,
)
from src.extract.check_data_sources import check_data_sources
from src.extract.load_to_dataframe import load_parquet_to_dataframe
from src.logger import setup_logger

logger = setup_logger("extract", "extract.log")


def extract_data() -> list[pl.DataFrame]:
    """Extracts data from CSV files and loads into dataframes.

    Returns:
        A list of dataframes containing the extracted data.
    """
    try:
        logger.info("Starting data extraction")
        files = [DISRUPTIONS_FILE, STATIONS_FILE, SERVICES_FILE]
        for file in files:
            check_data_sources(RAW_DATA_FILE_PATH, file)
        use_cols = [DISRUPTIONS_USECOLS, STATIONS_USECOLS, SERVICES_USECOLS]
        dataframes = []
        for i in range(3):
            parquet_file = files[i]["file_name"] + ".parquet"
            df = load_parquet_to_dataframe(
                RAW_DATA_FILE_PATH, parquet_file, use_cols[i]
            )
            dataframes.append(df)
        return dataframes
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise
