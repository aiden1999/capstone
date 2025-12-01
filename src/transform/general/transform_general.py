import pandas as pd

from src.logger import setup_logger
from src.transform.general.transform_01 import transform_01

logger = setup_logger(__name__, "transform.log")


def transform_general(df: pd.DataFrame) -> list[pd.DataFrame]:
    df_01 = transform_01(df)
    return [df_01]
