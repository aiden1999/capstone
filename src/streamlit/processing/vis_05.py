"""Background processing for visualisation 05."""

import pandas as pd

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe


def get_data_05() -> pd.DataFrame:
    """Loads the data needed for visualisation 05 into a DataFrame.

    Returns:
        DataFrame with the needed data.
    """
    df_05 = load_to_dataframe(OUTPUT_PATH, "03.csv")
    return df_05


def get_data_05_operators_grouped(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms DataFrame to be grouped by operator.

    Args:
        df: DataFrame with the original data.

    Returns:
        Transformed DataFrame.
    """
    df_05_operators = df.copy()
    df_05_operators.drop(columns=["Service:Type"], inplace=True)
    df_05_operators_grouped = df_05_operators.groupby(
        "Service:Company", as_index=False
    )["route_count"].sum()
    return df_05_operators_grouped


def get_data_05_operators_other(df: pd.DataFrame) -> pd.DataFrame:
    """Groups operators with less than 20,000 services into other, for use with
    the pie chart.

    Args:
        df: DataFrame with the original data.

    Returns:
        Transformed DataFrame.
    """
    df_05_operators_other = df.copy()
    df_05_operators_other.loc[
        df_05_operators_other["route_count"] < 20000, "Service:Company"
    ] = "Other operators"
    return df_05_operators_other


def get_data_05_service_type(df: pd.DataFrame, chosen_operator) -> pd.DataFrame:
    """Transforms DataFrame to contain just the services for the chosen operator.

    Args:
        chosen_operator (str): String representing the chosen operator - needs
            to exactly match a value in Service:Company.
        df: DataFrame with the original data.

    Returns:
        Transformed DataFrame.
    """
    operator_mask = df["Service:Company"] == chosen_operator
    df_05_service_type = df[operator_mask]
    df_05_service_type = df_05_service_type.rename(
        {"Service:Type": "service_type"}, axis=1
    )
    return df_05_service_type
