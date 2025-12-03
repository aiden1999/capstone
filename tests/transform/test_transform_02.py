import pandas as pd
import pytest

from src.transform.general.transform_02 import (
    create_columns,
    keep_start_and_end_stations,
    merge_rows,
)


def test_keep_start_and_end_stations_works():
    test_df = pd.DataFrame(
        {"Stop:Arrival time": [None, 123, 456], "Stop:Departure time": [12, 34, None]}
    )
    expected_df = pd.DataFrame(
        {"Stop:Arrival time": [None, 456], "Stop:Departure time": [12, None]}
    )
    actual_df = keep_start_and_end_stations(test_df)
    pd.testing.assert_frame_equal(expected_df, actual_df)


def test_keep_start_and_end_stations_returns_exception():
    test_df = pd.DataFrame({"a column": [1, 2, 3]})
    with pytest.raises(Exception):
        keep_start_and_end_stations(test_df)


def test_create_columns_works():
    test_df = pd.DataFrame(
        {
            "Stop:Arrival time": [None, 456],
            "Stop:Departure time": [12, None],
            "Stop:Station name": ["A", "B"],
        }
    )
    test_old_columns = ["Stop:Station name"]
    test_new_columns = ["start_station"]
    expected_df = pd.DataFrame(
        {
            "Stop:Arrival time": [None, 456],
            "Stop:Departure time": [12, None],
            "Stop:Station name": ["A", "B"],
            "start_station": ["A", None],
        }
    )
    actual_df = create_columns(
        test_df, test_old_columns, test_new_columns, "Stop:Departure time"
    )
    pd.testing.assert_frame_equal(actual_df, expected_df)
    pass


def test_create_columns_returns_exception():
    test_df = pd.DataFrame(
        {
            "Stop:Arrival time": [None, 456],
            "Stop:Departure time": [12, None],
            "Stop:Station name": ["A", "B"],
        }
    )
    test_old_columns = ["Stop:Station"]
    test_new_columns = ["start_station"]
    with pytest.raises(Exception):
        create_columns(
            test_df, test_old_columns, test_new_columns, "Stop: Departure time"
        )
    pass


def test_merge_rows_works():
    test_df = pd.DataFrame(
        {
            "Service:RDT-ID": [1, 1],
            "Stop:Arrival time": [None, 456],
            "Stop:Departure time": [12, None],
            "start_station": ["A", None],
            "end_station": [None, "B"],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Service:RDT-ID": [1],
            "Stop:Arrival time": [456],
            "Stop:Departure time": [12],
            "start_station": ["A"],
            "end_station": ["B"],
        }
    )
    actual_df = merge_rows(test_df)
    pd.testing.assert_frame_equal(expected_df, actual_df, check_dtype=False)


def test_merge_rows_returns_exception():
    test_df = pd.DataFrame(
        {
            "Stop:Arrival time": [None, 456],
            "Stop:Departure time": [12, None],
            "start_station": ["A", None],
            "end_station": [None, "B"],
        }
    )
    with pytest.raises(Exception):
        merge_rows(test_df)
