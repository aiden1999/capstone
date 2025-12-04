"""Loading a CSV into a DataFrame for later usage in transform."""

import os

import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "extract.log")


def load_to_dataframe(dir_path: str, file: str) -> pd.DataFrame:
    """Loads a CSV file into a DataFrame.

    Args:
        dir_path: String representing the directory path of the CSV file.
        file: String representing the CSV file.

    Returns:
        The DataFrame the CSV has been loaded into.
    """
    logger.info(f"Loading {file} into DataFrame")
    csv_path = os.path.join(dir_path, file)
    try:
        df = pd.read_csv(csv_path)
        logger.info(f"Loaded {file} into DataFrame")
        return df
    except Exception as e:
        logger.error(f"Failed to load {file} into DataFrame: {e}")
        raise
