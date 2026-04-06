"""Background processing for visualisation 01."""

import humanize

from src.extract.load_to_dataframe import load_csv_to_dataframe
from src.streamlit.processing.constants import OUTPUT_PATH


def get_data_01() -> str:
    """Loads the data needed for visualisation 05 and formats to have commas.

    Returns:
        String of the needed data.
    """
    df_01 = load_csv_to_dataframe(OUTPUT_PATH, "01.csv", ["total_planned_services"])
    value_01 = df_01["total_planned_services"][0]
    value_01 = humanize.intcomma(value_01)
    return value_01
