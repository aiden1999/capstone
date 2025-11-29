import pandas as pd
import pytest

from src.transform.transform import remove_international_data


def test_remove_international_data_works():
    test_df = pd.DataFrame({"id": [1, 2, 3], "country": ["B", "NL", "LUX"]})
    expected_df = pd.DataFrame({"id": [2, 3], "country": ["NL", "LUX"]})
    return_df = remove_international_data(test_df)
    print(expected_df)
    print(return_df)
    pd.testing.assert_frame_equal(expected_df, return_df)


def test_remove_international_data_raises_exception():
    test_df = pd.DataFrame({"id": [1, 2, 3], "code": ["B", "NL", "LUX"]})
    with pytest.raises(Exception):
        remove_international_data(test_df)
