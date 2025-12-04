import folium
import pandas as pd

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe
from src.streamlit.processing.constants import MAP_CENTER, RED


def get_data_02() -> pd.DataFrame:
    df_02 = load_to_dataframe(OUTPUT_PATH, "02.csv")
    df_02.sort_values("route_count", ascending=False, inplace=True)
    return df_02


def get_map(df: pd.DataFrame) -> folium.Map:
    map = folium.Map(location=MAP_CENTER, zoom_start=7)
    for _, row in df.iterrows():
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
