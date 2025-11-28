import os
import pandas as pd
from src.extract.check_data_sources import check_data_sources

RAW_DATA_FILE_PATH = "data/raw"
DISRUPTIONS_RAW_FILE = "disruptions-2024.csv"
STATIONS_RAW_FILE = "stations-2023-09.csv"
SERVICES_GZIP_FILE = "services-2024.csv.gz"
SERVICES_RAW_FILE = "services-2024.csv"


def extract_data():
    check_data_sources(RAW_DATA_FILE_PATH, SERVICES_RAW_FILE, SERVICES_GZIP_FILE)
    return 0  # placeholder
