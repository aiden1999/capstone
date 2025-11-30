import pandas as pd
import pytest

from src.transform.disruptions import drop_non_ns_services


def test_drop_ns_services_works():
    test_df = pd.DataFrame({"Service:Company": ["NS", "Arriva", "Blauwnet", "NS"]})
    expected_df = pd.DataFrame({"Service:Company": ["NS", "NS"]})
    ns_df = drop_non_ns_services(test_df)
    pd.testing.assert_frame_equal(ns_df, expected_df)


def test_drop_ns_services_returns_exception():
    test_df = pd.DataFrame({"Service:Operator": ["NS", "Arriva", "Blauwnet"]})
    with pytest.raises(Exception):
        drop_non_ns_services(test_df)
