"""Transformation for visualisation 01."""

import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def transform_01(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms data needed for visualisation 01.

    Counts the number of unique service IDs and puts that number into a DataFrame.

    Args:
        df: DataFrame for general statistics.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Transforming for 01")
    num_services = df["Service:RDT-ID"].nunique()
    transformed_df = pd.DataFrame({"total_planned_services": [num_services]})
    logger.info("Successfully transformed for 01")
    return transformed_df
