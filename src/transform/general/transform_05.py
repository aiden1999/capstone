"""Transformation for visualisation 05."""

import pandas as pd

from src.logger import setup_logger
from src.transform.utils import count_services, keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_05(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms data needed for visualisation 05.

    Args:
        df: DataFrame for general statistics.

    Returns:
        Transformed DataFrame.
    """
    df_needed_columns = keep_columns(
        df, ["Service:RDT-ID", "Service:Type", "Service:Company"]
    )
    df_no_duplicates = df_needed_columns.drop_duplicates()
    group_by_cols = ["Service:Type", "Service:Company"]
    count_services(df_no_duplicates, group_by_cols)
    transformed_df = df_no_duplicates.drop(columns=["Service:RDT-ID"])
    transformed_df.drop_duplicates(inplace=True)
    transformed_df.reset_index(drop=True, inplace=True)
    return transformed_df
