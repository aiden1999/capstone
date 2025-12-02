import pandas as pd
import pytest

from src.extract.load_to_dataframe import load_to_dataframe


def test_load_to_dataframe_returns_df():
    dir_path = "data/raw"
    file = "stations-2023-09.csv"
    df = load_to_dataframe(dir_path, file)
    assert isinstance(df, pd.DataFrame)


def test_load_to_dataframe_raises_exception():
    dir_path = "data/test"
    file = "non_existent.txt"
    with pytest.raises(Exception):
        load_to_dataframe(dir_path, file)
