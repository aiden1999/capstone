"""Transformation for visualisation 03"""

import polars as pl

from src.logger import setup_logger
from src.constants import VIS_03_COLUMNS
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
    df_needed_cols = keep_columns(df, VIS_03_COLUMNS)
    df_imploded_rows = implode_rows(df_needed_cols, "Service:RDT-ID")
    df_no_dups = df_imploded_rows.unique(subset="Stop:Station code")
    df_no_dups = df_no_dups.with_columns(
        pl.col("Stop:Station code").list.len().alias("Total stops")
    )
    return df_no_dups
