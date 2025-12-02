import pandas as pd
import pytest

from src.transform.utils import drop_columns, explode_row, merge_dataframes

test_df = pd.DataFrame(
    {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
)


def test_explode_row_works():
    column = "pets"
    expected_df = pd.DataFrame(
        {
            "id": [1, 1, 2, 2],
            "name": ["Alice", "Alice", "Bob", "Bob"],
            "pets": ["dog", "cat", "fish", "rabbit"],
        }
    )
    returned_df = explode_row(test_df, column)
    pd.testing.assert_frame_equal(returned_df, expected_df)


def test_explode_row_returns_exception():
    column = "age"
    with pytest.raises(Exception):
        explode_row(test_df, column)


test_df_1 = pd.DataFrame(
    {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
)
test_df_2 = pd.DataFrame({"id": [1, 2, 3], "country": ["England", "Wales", "Scotland"]})


def test_merge_dataframes_works():
    expected_df = pd.DataFrame(
        {
            "id": [1, 2],
            "name": ["Alice", "Bob"],
            "pets": ["dog,cat", "fish,rabbit"],
            "country": ["England", "Wales"],
        }
    )
    join_column = "id"
    returned_df = merge_dataframes(test_df_1, test_df_2, join_column, join_column)
    pd.testing.assert_frame_equal(returned_df, expected_df)


def test_merge_dataframes_returns_exception():
    join_column = "age"
    with pytest.raises(Exception):
        merge_dataframes(test_df_1, test_df_2, join_column, join_column)


def test_drop_columns_works():
    test_df = pd.DataFrame(
        {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
    )
    columns = ["id", "name"]
    expected_df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    test_df = drop_columns(test_df, columns)
    pd.testing.assert_frame_equal(test_df, expected_df)
