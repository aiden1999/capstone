import polars as pl
import polars.testing as pl_testing

from src.transform.general.transform_03 import transform_03


def test_transform_03_works():
    test_df = pl.DataFrame(
        {
            "Service:RDT-ID": [1, 1, 1, 2, 2, 3, 3, 3, 3],
            "Stop:Station code": ["A", "B", "C", "C", "D", "D", "C", "B", "A"],
            "Stop:Station name": ["a", "b", "c", "c", "d", "d", "c", "b", "a"],
            "geo_lat": [1, 2, 3, 3, 4, 4, 3, 2, 1],
            "geo_lng": [5, 6, 7, 7, 8, 8, 7, 6, 5],
            "Service:Partly cancelled": [False, True, False],
        }
    )
    expected_df = pl.DataFrame(
        {
            "Service:RDT-ID": [1, 2, 3],
            "Stop:Station code": ["A, B, C", "C, D", "D, C, B, A"],
            "Stop:Station name": ["a, b, c", "c, d", "d, c, b, a"],
            "geo_lat": ["1, 2, 3", "3, 4", "4, 3, 2, 1"],
            "geo_lng": ["5, 6, 7", "7, 8", "8, 7, 6, 5"],
            "Total stops": [3, 2, 4],
        }
    )
    actual_df = transform_03(test_df)
    pl_testing.assert_frame_equal(expected_df, actual_df, check_dtypes=False)
