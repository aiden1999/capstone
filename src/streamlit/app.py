"""Setup and run the Streamlit app."""

import sys
from pathlib import Path
import streamlit as st

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
general_page = st.Page("pages/general.py", title="General Statistics", icon="🇳🇱")

pages = st.navigation([general_page])
pages.run()
