"""Transformation for visualisation 02."""

import polars as pl

from src.constants import VIS_02_COLUMNS
from src.logger import setup_logger
from src.transform.utils import count_services, keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_02(df: pl.DataFrame) -> pl.DataFrame:
    """Transforms data needed for visualisation 02.

    Args:
        df: DataFrame for general statistics.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Transforming for 02")
    df = keep_start_and_end_stations(df)
    old_columns = ["Stop:Station name", "geo_lat", "geo_lng"]
    new_columns_start = ["start_station", "start_lat", "start_lng"]
    new_columns_end = ["end_station", "end_lat", "end_lng"]
    df_with_start = create_columns(
        df, old_columns, new_columns_start, "Stop:Departure time"
    )
    df_with_end = create_columns(
        df_with_start, old_columns, new_columns_end, "Stop:Arrival time"
    )
    df_needed_cols = keep_columns(df_with_end, VIS_02_COLUMNS)
    df_merged_rows = merge_rows(df_needed_cols)
    group_by_cols = ["Service:Type", "Service:Company", "start_station", "end_station"]
    count_services(df_merged_rows, group_by_cols)
    df_merged_rows.drop(columns=["Service:RDT-ID"], inplace=True)
    transformed_df = df_merged_rows.drop_duplicates()
    transformed_df.dropna(axis="index", inplace=True)
    transformed_df.reset_index(inplace=True, drop=True)
    logger.info("Successfully transformed for 02")
    return transformed_df


def keep_start_and_end_stations(df: pl.DataFrame) -> pl.DataFrame:
    """Removes records of intermediate stops.

    Intermediate stops have both an arrival time and departure time, so those
    records are dropped.

    Args:
        df: DataFrame with the original general statistics data.

    Returns:
        DataFrame of only start and end stops.
    """
    logger.info("Removing intermediate stations")
    try:
        start_end_mask = (
            df["Stop:Arrival time"].is_null() | df["Stop:Departure time"].is_null()
        )
        start_end_df = df[start_end_mask]
        logger.info("Successfully removed intermediate stations")
        return start_end_df
    except Exception as e:
        logger.error(f"Remove intermediate stations failed: {e}")
        raise


def create_columns(
    df: pl.DataFrame, old_cols: list[str], new_cols: list[str], cond_col: str
) -> pl.DataFrame:
    """Creates columns with more descriptive names.

    For example, for the rows that have a departure time (start stops), for
    every new column, the new column is filled with nulls, and the rows with
    start stops populate the new columns, i.e.:
    Stop:Station name -> start_station
    geo_lat -> start_lat
    geo_lng -> start_lng

    Args:
        df: DataFrame of start and end stations.
        old_cols: List of columns that the new columns are getting their data from.
        new_cols: List of columns to be created.
        cond_col: Column that is used to indicate whether the station is at the
            start or the end.

    Returns:
        DataFrame with new columns.
    """
    logger.info(f"Creating new columns: {new_cols}")
    try:
        new_df = df.clone()
        mask = new_df[cond_col].is_not_null()
        new_df = new_df.with_columns(
            [
                pl.when(mask)
                .then(pl.col(old_cols[i]))
                .otherwise(None)
                .alias(new_cols[i])
                for i in range(len(old_cols))
            ]
        )
        logger.info("Successfully created new columns")
        return new_df
    except Exception as e:
        logger.error(f"Create new columns failed: {e}")
        raise


def merge_rows(df: pl.DataFrame) -> pl.DataFrame:
    """Merge rows so that a record has no nulls in start_station, start_lat,
    start_lng, end_station, end_lat, end_lng.

    Args:
        df: DataFrame with nulls.

    Returns:
        Merged DataFrame.
    """
    logger.info("Merging rows")
    try:
        merged_df = df.group_by("Service:RDT-ID").first()
        logger.info("Successfully merged rows")
        return merged_df
    except Exception as e:
        logger.error(f"Merge rows failed: {e}")
        raise
