"""Extraction phase of the ETL process.

Called in run_etl.
"""

import pandas as pd

from src.constants import (
    DISRUPTIONS_RAW_FILE,
    RAW_DATA_FILE_PATH,
    SERVICES_GZIP_FILE,
    SERVICES_RAW_FILE,
    STATIONS_RAW_FILE,
)
from src.extract.check_data_sources import check_data_sources
from src.extract.load_to_dataframe import load_to_dataframe
from src.logger import setup_logger

logger = setup_logger("extract", "extract.log")


def extract_data() -> list[pd.DataFrame]:
    """Extracts data from CSV files and loads into dataframes.

    Returns:
        A list of dataframes containing the extracted data.
    """
    try:
        logger.info("Starting data extraction")
        check_data_sources(RAW_DATA_FILE_PATH, SERVICES_RAW_FILE, SERVICES_GZIP_FILE)
        csv_files = [DISRUPTIONS_RAW_FILE, STATIONS_RAW_FILE, SERVICES_RAW_FILE]
        dataframes = []
        for file in csv_files:
            df = load_to_dataframe(RAW_DATA_FILE_PATH, file)
            dataframes.append(df)
        logger.info("Finished data extraction")
        return dataframes
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise
