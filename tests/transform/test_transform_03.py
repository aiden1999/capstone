import pandas as pd

from src.transform.general.transform_03 import transform_03


def test_transform_01_works():
    test_df = pd.DataFrame(
        {
            "Service:RDT-ID": [1, 1, 1, 2, 2, 3, 3],
            "Stop:Station code": ["A", "B", "C", "C", "D", "D", "C"],
            "Stop:Station name": ["a", "b", "c", "c", "d", "d", "c"],
            "geo_lat": [1, 2, 3, 3, 4, 4, 3],
            "geo_lng": [5, 6, 7, 7, 8, 8, 7],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Service:RDT-ID": [1, 2, 3],
            "Stop:Station code": [["A", "B", "C"], ["C", "D"], ["D", "C"]],
            "Stop:Station name": [["a", "b", "c"], ["c", "d"], ["d", "c"]],
            "geo_lat": [[1, 2, 3], [3, 4], [4, 3]],
            "geo_lng": [[5, 6, 7], [7, 8], [8, 7]],
            "Total stops": [3, 2, 2],
        }
    )
    actual_df = transform_03(test_df)
    pd.testing.assert_frame_equal(expected_df, actual_df)
