"""Utilities for transform."""

import polars as pl

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def explode_row(df: pl.DataFrame, column: str) -> pl.DataFrame:
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
        df_exploded[column] = df_exploded[column].str.strip_chars()
        logger.info("Explode succeeded")
        return df_exploded
    except Exception as e:
        logger.error(f"Explode failed: {e}")
        raise


def merge_dataframes(
    df_1: pl.DataFrame, df_2: pl.DataFrame, col_1: str, col_2: str
) -> pl.DataFrame:
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
        merged_df = df_1.join(df_2, left_on=col_1, right_on=col_2)
        logger.info("Merge succeeded")
        return merged_df
    except Exception as e:
        logger.error(f"Merge failed: {e}")
        raise


def keep_columns(df: pl.DataFrame, keep_columns: list[str]) -> pl.DataFrame:
    """Drops columns that aren't listed to keep.

    Args:
        df: Input DataFrame.
        keep_columns: List of strings representing columns to be kept.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Dropping columns")
    new_df = df.select([col for col in keep_columns if col in df.columns])
    logger.info("Dropped columns successfully")
    return new_df


def count_services(df: pl.DataFrame, group_by_cols: list[str]):
    """Counts the number of services based on the group by.

    Args:
        df: Input DataFrame.
        group_by_cols: List of strings representing the columns for the group by.
    """
    logger.info("Counting services")
    try:
        df = df.with_columns(pl.len().over(group_by_cols).alias("route_count"))
        df = df.with_columns(pl.col("route_count").fill_null(1).cast(pl.Int32))
        logger.info("Successfully counted services")
    except Exception as e:
        logger.error(f"Count services failed: {e}")
        raise


def implode_rows(df: pl.DataFrame, index_col: str) -> pl.DataFrame:
    """Merges rows based on a shared index.

    Args:
        df: Input DataFrame.
        index_col: Shared index.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Imploding rows")
    try:
        new_df = df.group_by(index_col, maintain_order=True).agg(pl.all())
        logger.info("Imploded rows successfully")
        return new_df
    except Exception as e:
        logger.error(f"Implode rows failed: {e}")
        raise
