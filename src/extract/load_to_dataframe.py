"""Loading a CSV into a DataFrame for later usage in transform."""

import os

import polars as pl

from src.logger import setup_logger

logger = setup_logger(__name__, "extract.log")


def load_to_dataframe(dir_path: str, file: str, use_cols: list[str]) -> pl.DataFrame:
    """Loads a CSV file into a DataFrame.

    Args:
        dir_path: String representing the directory path of the CSV file.
        file: String representing the CSV file.
        use_cols: List of the columns to be read.

    Returns:
        The DataFrame the CSV has been loaded into.
    """
    logger.info(f"Loading {file} into DataFrame")
    csv_path = os.path.join(dir_path, file)
    try:
        df = pl.read_csv(csv_path, columns=use_cols)
        logger.info(f"Loaded {file} into DataFrame")
        return df
    except Exception as e:
        logger.error(f"Failed to load {file} into DataFrame: {e}")
        raise
