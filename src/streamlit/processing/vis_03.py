"""[TODO:description]

[TODO:description]
"""

import polars as pl

from src.extract.load_to_dataframe import load_csv_to_dataframe
from src.streamlit.processing.constants import COLUMNS_03, OUTPUT_PATH


def get_data_03() -> pl.DataFrame:
    df_03 = load_csv_to_dataframe(OUTPUT_PATH, "03.csv", COLUMNS_03)
    return df_03
