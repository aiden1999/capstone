"""Transformation for visualisation 03"""

import polars as pl

from src.logger import setup_logger
from src.transform.constants import VIS_03_COLUMNS
from src.transform.utils import implode_rows, keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_03(df: pl.DataFrame) -> pl.DataFrame:
    """Transforms data needed for visualisation 03.

    Args:
        df: DataFrame for general statistics.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Transforming for 03")
    df = keep_columns(df, VIS_03_COLUMNS)
    print(df.head())
    df = df.filter(not pl.col("Service:Partly cancelled"))
    df = implode_rows(df, "Service:RDT-ID")
    df = df.unique(subset="Stop:Station code")
    df = df.with_columns(
        pl.col("Stop:Station code").list.len().alias("Total stops")
    ).sort("Total stops")  # sorting only so that tests pass
    df = df.with_columns(
        pl.col("Stop:Station code", "Stop:Station name").list.join(", "),
        pl.col("geo_lat", "geo_lng")
        .list.eval(pl.element().cast(pl.String))
        .list.join(", "),
    ).drop("Service:Partly cancelled")
    return df
