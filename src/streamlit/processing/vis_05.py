import pandas as pd

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe


def get_data_05() -> pd.DataFrame:
    df_05 = load_to_dataframe(OUTPUT_PATH, "03.csv")
    return df_05


def get_data_05_operators_grouped(df: pd.DataFrame) -> pd.DataFrame:
    df_05_operators = df.copy()
    df_05_operators.drop(columns=["Service:Type"], inplace=True)
    df_05_operators_grouped = df_05_operators.groupby(
        "Service:Company", as_index=False
    )["route_count"].sum()
    return df_05_operators_grouped


def get_data_05_operators_other(df: pd.DataFrame) -> pd.DataFrame:
    df_05_operators_other = df.copy()
    df_05_operators_other.loc[
        df_05_operators_other["route_count"] < 20000, "Service:Company"
    ] = "Other operators"
    return df_05_operators_other


def get_data_05_service_type(df: pd.DataFrame, chosen_operator) -> pd.DataFrame:
    operator_mask = df["Service:Company"] == chosen_operator
    df_05_service_type = df[operator_mask]
    df_05_service_type = df_05_service_type.rename(
        {"Service:Type": "service_type"}, axis=1
    )
    return df_05_service_type
