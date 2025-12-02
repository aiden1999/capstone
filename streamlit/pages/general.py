import os
import sys

import folium
import humanize
from streamlit_folium import st_folium

import streamlit as st

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_DIR)

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe

df_01 = load_to_dataframe(OUTPUT_PATH, "01.csv")
value_01 = df_01.loc[0, "total_planned_services"]
value_01 = humanize.intcomma(value_01)

df_02 = load_to_dataframe(OUTPUT_PATH, "02.csv")
df_02.sort_values("route_count", ascending=False, inplace=True)

st.title("Domestic Dutch Rail Services for 2024")
st.header("General Statistics")

st.subheader("Total planned services")
st.metric("Planned services", value_01)

st.subheader("Most and least frequent routes")
column_config_02 = {
    "Service:Type": "Type",
    "Service:Company": "Operator",
    "start_station": "Start Station",
    "start_lat": None,
    "start_lng": None,
    "end_station": "End Station",
    "end_lat": None,
    "end_lng": None,
    "route_count": "Route Count",
}
st.dataframe(data=df_02, hide_index=True, column_config=column_config_02)

num_routes = st.slider(
    "Choose a number to display", min_value=5, max_value=20, value=10, step=1
)
df_02_top = df_02.head(num_routes)
df_02_bottom = df_02.tail(num_routes)
red = "#ad1d25"
map_center = [52, 6]
map_icon = (
    folium.plugins.BeautifyIcon(
        icon="circle",
        background_color=red,
        border_color=red,
        text_color=red,
        border_width=1,
    ),
)


col_most, col_least = st.columns(2)
with col_most:
    st.markdown("#### Most frequent")
    map_most = folium.Map(location=map_center, zoom_start=7)
    for _, row in df_02_top.iterrows():
        start_point = [row["start_lat"], row["start_lng"]]
        end_point = [row["end_lat"], row["end_lng"]]
        folium.Marker(
            start_point,
            popup=row["start_station"],
            icon=folium.plugins.BeautifyIcon(
                icon="circle",
                background_color=red,
                border_color=red,
                text_color=red,
                border_width=1,
            ),
        ).add_to(map_most)
        folium.Marker(
            end_point,
            popup=row["end_station"],
            icon=folium.plugins.BeautifyIcon(
                icon="circle",
                background_color=red,
                border_color=red,
                text_color=red,
                border_width=1,
            ),
        ).add_to(map_most)
        folium.PolyLine(
            locations=[start_point, end_point], color=red, weight=2, opacity=1
        ).add_to(map_most)
    st_folium(map_most)
with col_least:
    st.markdown("#### Least frequent")
    map_least = folium.Map(location=map_center, zoom_start=7)
    for _, row in df_02_bottom.iterrows():
        start_point = [row["start_lat"], row["start_lng"]]
        end_point = [row["end_lat"], row["end_lng"]]
        folium.Marker(
            start_point,
            popup=row["start_station"],
            icon=folium.plugins.BeautifyIcon(
                icon="circle",
                background_color=red,
                border_color=red,
                text_color=red,
                border_width=1,
            ),
        ).add_to(map_least)
        folium.Marker(
            end_point,
            popup=row["end_station"],
            icon=folium.plugins.BeautifyIcon(
                icon="circle",
                background_color=red,
                border_color=red,
                text_color=red,
                border_width=1,
            ),
        ).add_to(map_least)
        folium.PolyLine(
            locations=[start_point, end_point], color=red, weight=2, opacity=1
        ).add_to(map_least)
    st_folium(map_least)
