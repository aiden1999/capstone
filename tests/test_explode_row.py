import pandas as pd
import pytest

from src.transform.explode_row import explode_row

test_df = pd.DataFrame(
    {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
)


def test_explode_row_works():
    column = "pets"
    exploded_df = pd.DataFrame(
        {
            "id": [1, 1, 2, 2],
            "name": ["Alice", "Alice", "Bob", "Bob"],
            "pets": ["dog", "cat", "fish", "rabbit"],
        }
    )
    returned_df = explode_row(test_df, column)
    pd.testing.assert_frame_equal(returned_df, exploded_df)


def test_explode_row_returns_exception():
    column = "age"
    with pytest.raises(Exception):
        explode_row(test_df, column)
