"""Load DataFrames into CSVs."""

import pandas as pd
import os

from src.logger import setup_logger

logger = setup_logger("load", "load.log")


def load_data(dfs: list[list[pd.DataFrame]], dir_path: str):
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
                file_path = os.path.join(dir_path, file_name)
                df.to_csv(file_path, index=False)
                count += 1
        logger.info("Finished data loading")
    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
