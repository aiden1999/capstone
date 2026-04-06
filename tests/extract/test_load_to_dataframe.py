import polars as pl
import pytest

from src.extract.constants import STATIONS_USECOLS
from src.extract.load_to_dataframe import (
    load_csv_to_dataframe,
    load_parquet_to_dataframe,
)


def test_load_csv_to_dataframe_returns_df():
    dir_path = "data/raw"
    file = "stations-2023-09.csv"
    use_cols = STATIONS_USECOLS
    df = load_csv_to_dataframe(dir_path, file, use_cols)
    assert isinstance(df, pl.DataFrame)


def test_load_csv_to_dataframe_raises_exception():
    dir_path = "data/test"
    file = "non_existent.txt"
    use_cols = ["something"]
    with pytest.raises(Exception):
        load_csv_to_dataframe(dir_path, file, use_cols)


def test_load_parquet_to_dataframe_returns_df():
    dir_path = "data/raw"
    file = "stations-2023-09.parquet"
    use_cols = STATIONS_USECOLS
    df = load_parquet_to_dataframe(dir_path, file, use_cols)
    assert isinstance(df, pl.DataFrame)


def test_load_parquet_to_dataframe_raises_exception():
    dir_path = "data/test"
    file = "non_existent.txt"
    use_cols = ["something"]
    with pytest.raises(Exception):
        load_parquet_to_dataframe(dir_path, file, use_cols)
