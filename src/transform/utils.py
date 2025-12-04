"""Utilities for transform."""

import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def explode_row(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Explodes a row on a column with comma separated values.

    Turns the values in the columns into a list of strings, which are then
    exploded so one value per row, and whitespace is stripped.

    Args:
        df: DataFrame to be transformed.
        column: String representing the column with the comman separated values.

    Returns:
        DataFrame with more rows.
    """
    logger.info(f"Exploding dataframe on column {column}")
    try:
        df[column] = df[column].str.split(",")
        df_exploded = df.explode(column)
        df_exploded[column] = df_exploded[column].str.strip()
        df_exploded = df_exploded.reset_index(drop=True)
        logger.info("Explode succeeded")
        return df_exploded
    except Exception as e:
        logger.error(f"Explode failed: {e}")
        raise


def merge_dataframes(
    df_1: pd.DataFrame, df_2: pd.DataFrame, col_1: str, col_2: str
) -> pd.DataFrame:
    """Inner merge of two DataFrames.

    Args:
        df_1: Left DataFrame.
        df_2: Right DataFrame.
        col_1: Left key for merge.
        col_2: Right key for merge.

    Returns:
        Merged DataFrame.
    """
    logger.info("Merging...")
    try:
        merged_df = df_1.merge(df_2, left_on=col_1, right_on=col_2)
        logger.info("Merge succeeded")
        return merged_df
    except Exception as e:
        logger.error(f"Merge failed: {e}")
        raise


def keep_columns(df: pd.DataFrame, keep_columns: list[str]) -> pd.DataFrame:
    """Drops columns that aren't listed to keep.

    Args:
        df: Input DataFrame.
        keep_columns: List of strings representing columns to be kept.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Dropping columns")
    new_df = df[df.columns.intersection(keep_columns)]
    logger.info("Dropped columns successfully")
    return new_df


def count_services(df: pd.DataFrame, group_by_cols: list[str]):
    """Counts the number of services based on the group by.

    Args:
        df: Input DataFrame.
        group_by_cols: List of strings representing the columns for the group by.
    """
    logger.info("Counting services")
    try:
        df["route_count"] = df.groupby(group_by_cols).transform("size")
        df["route_count"] = df["route_count"].fillna(1).astype("int")
        logger.info("Successfully counted services")
    except Exception as e:
        logger.error(f"Count services failed: {e}")
        raise
