"""Background processing for visualisation 01."""

import humanize

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe


def get_data_01() -> str:
    """Loads the data needed for visualisation 05 and formats to have commas.

    Returns:
        String of the needed data.
    """
    df_01 = load_to_dataframe(OUTPUT_PATH, "01.csv")
    value_01 = df_01.loc[0, "total_planned_services"]
    value_01 = humanize.intcomma(value_01)
    return value_01
