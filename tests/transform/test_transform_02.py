import pandas as pd

from src.transform.general.transform_02 import keep_start_and_end_stations


def test_keep_start_and_end_stations_works():
    test_df = pd.DataFrame(
        {"Stop:Arrival time": [None, 123, 456], "Stop:Departure time": [12, 34, None]}
    )
    expected_df = pd.DataFrame(
        {"Stop:Arrival time": [None, 456], "Stop:Departure time": [12, None]}
    )
    actual_df = keep_start_and_end_stations(test_df)
    pd.testing.assert_frame_equal(expected_df, actual_df)
