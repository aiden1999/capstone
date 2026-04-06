"""Background processing for visualisation 05."""

import folium
import polars as pl

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_csv_to_dataframe
from src.streamlit.processing.constants import COLUMNS_02, MAP_CENTER, RED


def get_data_02() -> pl.DataFrame:
    """Loads the data needed for visualisation 02 into a DataFrame.

    Returns:
        DataFrame with the needed data.
    """
    df_02 = load_csv_to_dataframe(OUTPUT_PATH, "02.csv", COLUMNS_02)
    df_02 = df_02.sort(by="route_count", descending=True)
    return df_02


def get_map(df: pl.DataFrame) -> folium.Map:
    """Creates a map with start points, end points, and lines connecting the
    two for showing the most and least frequent routes.

    Args:
        df: DataFrame with the needed data.

    Returns:
        A Folium map with the datapoints plotted.
    """
    map = folium.Map(location=MAP_CENTER, zoom_start=7)
    for row in df.iter_rows(named=True):
        start_point = [row["start_lat"], row["start_lng"]]
        end_point = [row["end_lat"], row["end_lng"]]
        folium.Marker(
            start_point,
            popup=row["start_station"],
            icon=folium.plugins.BeautifyIcon(
                icon="circle",
                background_color=RED,
                border_color=RED,
                text_color=RED,
                border_width=0,
            ),
        ).add_to(map)
        folium.Marker(
            end_point,
            popup=row["end_station"],
            icon=folium.plugins.BeautifyIcon(
                icon="circle",
                background_color=RED,
                border_color=RED,
                text_color=RED,
                border_width=0,
            ),
        ).add_to(map)
        folium.PolyLine(
            locations=[start_point, end_point], color=RED, weight=2, opacity=1
        ).add_to(map)
    return map
