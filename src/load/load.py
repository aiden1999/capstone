import pandas as pd
import os

from src.logger import setup_logger

logger = setup_logger("load", "load.log")


def load_data(dfs: list[list[pd.DataFrame]], dir_path):
    count = 1
    try:
        logger.info("Starting data loading")
        for category in dfs:
            for df in category:
                file_name = str(count).zfill(2)
                file_name += ".csv"
                file_path = os.path.join(dir_path, file_name)
                df.to_csv(file_path, index=False)
        logger.info("Finished data loading")
    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
