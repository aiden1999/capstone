import pandas as pd

from src.constants import VIS_02_COLUMNS
from src.logger import setup_logger
from src.transform.utils import keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_02(df: pd.DataFrame) -> pd.DataFrame:
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
    count_services(df_merged_rows)
    df_merged_rows.drop(columns=["Service:RDT-ID"], inplace=True)
    transformed_df = df_merged_rows.drop_duplicates()
    transformed_df.dropna(axis="index", inplace=True)
    transformed_df.reset_index(inplace=True, drop=True)
    logger.info("Successfully transformed for 02")
    return transformed_df


def keep_start_and_end_stations(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Removing intermediate stations")
    try:
        start_end_mask = (
            df["Stop:Arrival time"].isnull() | df["Stop:Departure time"].isnull()
        )
        start_end_df = df[start_end_mask]
        start_end_df.reset_index(drop=True, inplace=True)
        logger.info("Successfully removed intermediate stations")
        return start_end_df
    except Exception as e:
        logger.error(f"Remove intermediate stations failed: {e}")
        raise


def create_columns(
    df: pd.DataFrame, old_cols: list[str], new_cols: list[str], cond_col: str
) -> pd.DataFrame:
    logger.info(f"Creating new columns: {new_cols}")
    try:
        new_df = df.copy()
        mask = new_df[cond_col].notnull()
        for i in range(len(old_cols)):
            new_df.loc[:, new_cols[i]] = None
            new_df.loc[mask, new_cols[i]] = new_df.loc[mask, old_cols[i]]
        logger.info("Successfully created new columns")
        return new_df
    except Exception as e:
        logger.error(f"Create new columns failed: {e}")
        raise


def merge_rows(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Merging rows")
    try:
        merged_df = df.groupby("Service:RDT-ID", as_index=False).first()
        logger.info("Successfully merged rows")
        return merged_df
    except Exception as e:
        logger.error(f"Merge rows failed: {e}")
        raise


def count_services(df: pd.DataFrame):
    logger.info("Counting services")
    try:
        df["route_count"] = df.groupby(
            ["Service:Type", "Service:Company", "start_station", "end_station"]
        ).transform("size")
        df["route_count"] = df["route_count"].fillna(1).astype("int")
        logger.info("Successfully counted services")
    except Exception as e:
        logger.error(f"Count services failed: {e}")
        raise
