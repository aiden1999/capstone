import polars as pl
import polars.testing as pl_testing
import pytest

from src.transform.utils import (
    count_services,
    explode_row,
    implode_rows,
    keep_columns,
    merge_dataframes,
)

test_df = pl.DataFrame(
    {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
)


def test_explode_row_works():
    column = "pets"
    expected_df = pl.DataFrame(
        {
            "id": [1, 1, 2, 2],
            "name": ["Alice", "Alice", "Bob", "Bob"],
            "pets": ["dog", "cat", "fish", "rabbit"],
        }
    )
    returned_df = explode_row(test_df, column)
    pl_testing.assert_frame_equal(returned_df, expected_df)


def test_explode_row_returns_exception():
    column = "age"
    with pytest.raises(Exception):
        explode_row(test_df, column)


test_df_1 = pl.DataFrame(
    {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
)
test_df_2 = pl.DataFrame({"id": [1, 2, 3], "country": ["England", "Wales", "Scotland"]})


def test_merge_dataframes_works():
    expected_df = pl.DataFrame(
        {
            "id": [1, 2],
            "name": ["Alice", "Bob"],
            "pets": ["dog,cat", "fish,rabbit"],
            "country": ["England", "Wales"],
        }
    )
    join_column = "id"
    returned_df = merge_dataframes(test_df_1, test_df_2, join_column, join_column)
    pl_testing.assert_frame_equal(returned_df, expected_df)


def test_merge_dataframes_returns_exception():
    join_column = "age"
    with pytest.raises(Exception):
        merge_dataframes(test_df_1, test_df_2, join_column, join_column)


def test_keep_columns_works():
    test_df = pl.DataFrame(
        {"id": [1, 2], "name": ["Alice", "Bob"], "pets": ["dog,cat", "fish,rabbit"]}
    )
    columns = ["id", "name"]
    expected_df = pl.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    test_df = keep_columns(test_df, columns)
    pl_testing.assert_frame_equal(test_df, expected_df)


def test_count_services_works():
    test_df = pl.DataFrame(
        {
            "Service:Type": ["x", "x"],
            "Service:Company": ["y", "y"],
            "start_station": ["A", "A"],
            "end_station": ["B", "B"],
        }
    )
    test_col_list = ["Service:Type", "Service:Company", "start_station", "end_station"]
    expected_df = pl.DataFrame(
        {
            "Service:Type": ["x", "x"],
            "Service:Company": ["y", "y"],
            "start_station": ["A", "A"],
            "end_station": ["B", "B"],
            "route_count": [2, 2],
        }
    )
    actual_df = count_services(test_df, test_col_list)
    pl_testing.assert_frame_equal(left=expected_df, right=actual_df, check_dtypes=False)


def test_count_services_returns_exception():
    test_df = pl.DataFrame(
        {
            "Service:Type": ["x", "x"],
            "start_station": ["A", "A"],
            "end_station": ["B", "B"],
        }
    )
    test_col_list = ["start"]
    with pytest.raises(Exception):
        returned_df = count_services(test_df, test_col_list)


def test_implode_rows_works():
    test_df = pl.DataFrame(
        {
            "id_col": [1, 1, 1, 2, 2, 3, 3],
            "stn_code": ["A", "B", "C", "C", "D", "D", "C"],
            "stn_name": ["a", "b", "c", "c", "d", "d", "c"],
        }
    )
    test_index_col = "id_col"
    expected_df = pl.DataFrame(
        {
            "id_col": [1, 2, 3],
            "stn_code": [["A", "B", "C"], ["C", "D"], ["D", "C"]],
            "stn_name": [["a", "b", "c"], ["c", "d"], ["d", "c"]],
        }
    )
    returned_df = implode_rows(test_df, test_index_col)
    pl_testing.assert_frame_equal(expected_df, returned_df)
