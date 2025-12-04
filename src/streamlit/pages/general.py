import plotly.express as px
from streamlit_folium import st_folium

import streamlit as st
from src.streamlit.processing.constants import (
    COLUMN_CONFIG_02,
    COLUMN_CONFIG_05_OPERATORS,
    COLUMN_CONFIG_05_SERVICES,
    RED,
)
from src.streamlit.processing.vis_01 import get_data_01
from src.streamlit.processing.vis_02 import get_data_02, get_map
from src.streamlit.processing.vis_05 import (
    get_data_05,
    get_data_05_operators_grouped,
    get_data_05_operators_other,
    get_data_05_service_type,
)

st.title("Domestic Dutch Rail Services for 2024")
st.header("General Statistics")

st.divider()

st.subheader("Total planned services")

value_01 = get_data_01()
st.metric("Planned services", value_01)

st.divider()

st.subheader("Most and least frequent routes")

df_02 = get_data_02()
st.dataframe(data=df_02, hide_index=True, column_config=COLUMN_CONFIG_02)

num_routes = st.slider(
    "Choose a number to display", min_value=5, max_value=20, value=10, step=1
)
df_02_top = df_02.head(num_routes)
df_02_bottom = df_02.tail(num_routes)

col_most, col_least = st.columns(2)
with col_most:
    st.markdown("#### Most frequent")
    map_most = get_map(df_02_top)
    st_folium(map_most)
with col_least:
    st.markdown("#### Least frequent")
    map_least = get_map(df_02_bottom)
    st_folium(map_least)

st.divider()

st.subheader("Total services by operator")

df_05 = get_data_05()
df_05_operators_grouped = get_data_05_operators_grouped(df_05)
df_05_operators_other = get_data_05_operators_other(df_05_operators_grouped)

operator_fig = px.pie(
    df_05_operators_other, values="route_count", names="Service:Company"
)
st.plotly_chart(operator_fig)
st.dataframe(
    df_05_operators_grouped, hide_index=True, column_config=COLUMN_CONFIG_05_OPERATORS
)

st.markdown("#### Service types by operator")

chosen_operator = st.pills(
    "Choose an operator", df_05_operators_grouped["Service:Company"], default="NS"
)
df_05_service_type = get_data_05_service_type(df_05, chosen_operator)
st.bar_chart(
    df_05_service_type,
    x="service_type",
    y="route_count",
    x_label="Service type",
    y_label="Number of services",
    color=RED,
)
st.dataframe(
    df_05_service_type, hide_index=True, column_config=COLUMN_CONFIG_05_SERVICES
)
