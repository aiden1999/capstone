import pandas as pd
import pytest

from src.extract.check_data_sources import check_file_exists
from src.load.load import load_data


def test_load_data_creates_csv():
    test_df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    test_list = [[test_df]]
    dir_path = "data/test"
    expected_file = "01.csv"
    load_data(test_list, dir_path)
    file_exists = check_file_exists(dir_path, expected_file)
    assert file_exists


def test_load_data_returns_exception():
    test_data = "hello world"
    dir_path = "dir/path"
    with pytest.raises(Exception):
        load_data(test_data, dir_path)
