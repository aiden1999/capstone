"""Background processing for visualisation 05."""

import polars as pl

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe
from src.streamlit.processing.constants import COLUMNS_05


def get_data_05() -> pl.DataFrame:
    """Loads the data needed for visualisation 05 into a DataFrame.

    Returns:
        DataFrame with the needed data.
    """
    df_05 = load_to_dataframe(OUTPUT_PATH, "04.csv", COLUMNS_05)
    return df_05


def get_data_05_operators_grouped(df: pl.DataFrame) -> pl.DataFrame:
    """Transforms DataFrame to be grouped by operator.

    Args:
        df: DataFrame with the original data.

    Returns:
        Transformed DataFrame.
    """
    df_05_operators = df.clone()
    df_05_operators = (
        df_05_operators.group_by("Service:Company")
        .agg(pl.col("route_count").sum())
        .sort("route_count", descending=True)
    )
    return df_05_operators


def get_data_05_operators_other(df: pl.DataFrame) -> pl.DataFrame:
    """Groups operators with less than 20,000 services into other, for use with
    the pie chart.

    Args:
        df: DataFrame with the original data.

    Returns:
        Transformed DataFrame.
    """
    df_05_operators_other = df.clone()
    df_05_operators_other = df_05_operators_other.with_columns(
        pl.when(pl.col("route_count") < 20000)
        .then(pl.lit("Other operators"))
        .otherwise(pl.col("Service:Company"))
        .alias("Service:Company")
    )
    return df_05_operators_other


def get_data_05_service_type(df: pl.DataFrame, chosen_operator) -> pl.DataFrame:
    """Transforms DataFrame to contain just the services for the chosen operator.

    Args:
        chosen_operator (str): String representing the chosen operator - needs
            to exactly match a value in Service:Company.
        df: DataFrame with the original data.

    Returns:
        Transformed DataFrame.
    """
    df_05_service_type = (
        df.filter(pl.col("Service:Company") == chosen_operator)
        .rename({"Service:Type": "service_type"})
        .sort("service_type")
    )
    return df_05_service_type
