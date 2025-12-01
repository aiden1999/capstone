import os
import sys

import streamlit as st
import humanize

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_DIR)

from src.constants import OUTPUT_PATH
from src.extract.load_to_dataframe import load_to_dataframe

df_01 = load_to_dataframe(OUTPUT_PATH, "01.csv")
value_01 = df_01.loc[0, "total_planned_services"]
value_01 = humanize.intcomma(value_01)

st.title("Domestic Dutch Rail Services for 2024")
st.header("General Statistics")

st.metric("Total planned services", value_01)
