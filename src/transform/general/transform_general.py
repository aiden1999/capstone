"""Tranformation for general statistics."""

import polars as pl

from src.logger import setup_logger
from src.transform.general.transform_01 import transform_01
from src.transform.general.transform_02 import transform_02
from src.transform.general.transform_03 import transform_03
from src.transform.general.transform_05 import transform_05

logger = setup_logger(__name__, "transform.log")


def transform_general(df: pl.DataFrame) -> list[pl.DataFrame]:
    """Orchestrates the transformation of the general statistics DataFrame.

    Args:
        df: DataFrame with the needed columns for general statistics.

    Returns:
        List of transformed DataFrames.
    """
    df_01 = transform_01(df)
    df_02 = transform_02(df)
    df_03 = transform_03(df)
    df_05 = transform_05(df)
    return [df_01, df_02, df_03, df_05]
