"""Transformation for visualisation 03"""

import pandas as pd

from src.logger import setup_logger
from src.constants import VIS_03_COLUMNS
from src.transform.utils import implode_rows, keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_03(df: pd.DataFrame) -> pd.DataFrame:
    """[TODO:description]

    Args:
        df: [TODO:description]

    Returns:
        [TODO:return]
    """
    logger.info("Transforming for 03")
    df_needed_cols = keep_columns(df, VIS_03_COLUMNS)
    df_imploded_rows = implode_rows(df_needed_cols, "Service:RDT-ID")
    df_no_dups = df_imploded_rows.drop_duplicates(subset="Stop:Station code")
    df_no_dups.reset_index(inplace=True, drop=True)
    df_no_dups["Total stops"] = df_no_dups["Stop:Station code"].apply(len)
    return df_no_dups
