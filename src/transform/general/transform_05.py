"""Transformation for visualisation 05."""

import polars as pl

from src.logger import setup_logger
from src.transform.utils import count_services, keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_05(df: pl.DataFrame) -> pl.DataFrame:
    """Transforms data needed for visualisation 05.

    Args:
        df: DataFrame for general statistics.

    Returns:
        Transformed DataFrame.
    """
    df = keep_columns(df, ["Service:RDT-ID", "Service:Type", "Service:Company"])
    df = df.unique()  # each service is counted once
    group_by_cols = ["Service:Type", "Service:Company"]
    df = count_services(df, group_by_cols)
    df = df.drop("Service:RDT-ID").unique()
    return df
