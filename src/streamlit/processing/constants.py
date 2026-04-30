"""Constants for use with the Streamlit app."""

OUTPUT_PATH = "data/output"
RED = "#ad1d25"
MAP_CENTER = [52, 6]
COLUMNS_02 = [
    "Service:Type",
    "Service:Company",
    "start_station",
    "start_lat",
    "start_lng",
    "end_station",
    "end_lat",
    "end_lng",
    "route_count",
]
COLUMN_CONFIG_02 = {
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
COLUMNS_03 = ["Stop:Station name", "geo_lat", "geo_lng", "Total stops"]
COLUMNS_CONFIG_03 = {
    "Stop:Station name": "Stations",
    "geo_lat": None,
    "geo_lng": None,
    "Total stops": "Total stops",
}
COLUMNS_05 = ["Service:Type", "Service:Company", "route_count"]
COLUMN_CONFIG_05_OPERATORS = {
    "Service:Company": "Operator",
    "route_count": "Total services",
}
COLUMN_CONFIG_05_SERVICES = {
    "service_type": "Service type",
    "Service:Company": None,
    "route_count": "Total services",
}
