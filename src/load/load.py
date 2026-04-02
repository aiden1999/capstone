"""Load DataFrames into CSVs."""

import polars as pl
import os

from src.logger import setup_logger

logger = setup_logger("load", "load.log")


def load_data(dfs: list[list[pl.DataFrame]], dir_path: str):
    """Loads DataFrames into CSVs by looping through a list of lists of
    DataFrames, incrementing the name of the output CSV each time.

    Args:
        dfs: List of lists of DataFrames, to be loaded into CSVs.
        dir_path: String representing the directory path for the CSVs.
    """
    count = 1
    try:
        logger.info("Starting data loading")
        for category in dfs:
            for df in category:
                file_name = str(count).zfill(2)
                file_name += ".csv"
                logger.debug(f"Loading {file_name}")
                file_path = os.path.join(dir_path, file_name)
                df.write_csv(file_path)
                count += 1
    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
