import streamlit as st

general_page = st.Page("pages/general.py", title="General Statistics", icon="🏠")
# stations_page = st.Page(
#     "streamlit/stations.py", title="Station Statistics", icon="🚉"
# )
# dpcc_page = st.Page(
#     "streamlit/dpcc.py",
#     title="Delays, Platform Changes, and Cancellations",
#     icon="⚠️",
# )
# diruptions_page = st.Page(
#     "streamlit/disruptions.py", title="Disruption Statistics", icon="❌"
# )

pages = st.navigation([general_page])
pages.run()
