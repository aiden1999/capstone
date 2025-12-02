import pandas as pd

from src.transform.general.transform_01 import transform_01


def test_transform_01_returns_correct_number():
    test_df = pd.DataFrame({"Service:RDT-ID": [1, 1, 2, 3, 3, 3, 4, 5]})
    expected_output = pd.DataFrame({"total_planned_services": [5]})
    actual_output = transform_01(test_df)
    pd.testing.assert_frame_equal(expected_output, actual_output)
