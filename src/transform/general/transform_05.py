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
    df_needed_columns = keep_columns(
        df, ["Service:RDT-ID", "Service:Type", "Service:Company"]
    )
    df_no_duplicates = df_needed_columns.unique()
    group_by_cols = ["Service:Type", "Service:Company"]
    count_services(df_no_duplicates, group_by_cols)
    transformed_df = df_no_duplicates.drop("Service:RDT-ID")
    transformed_df.unique()
    return transformed_df
