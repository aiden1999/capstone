import os

import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "extract.log")


def load_to_dataframe(dir_path: str, file: str) -> pd.DataFrame:
    logger.info(f"Loading {file} into DataFrame")
    csv_path = os.path.join(dir_path, file)
    try:
        df = pd.read_csv(csv_path)
        logger.info(f"Loaded {file} into DataFrame")
        return df
    except Exception as e:
        logger.error(f"Failed to load {file} into DataFrame: {e}")
        raise
