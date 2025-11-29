import pandas as pd

from src.logger import setup_logger
from src.transform import explode_row

logger = setup_logger("transform", "transform.log")


def transform(extracted_data: list[pd.DataFrame]):
    disruptions_raw, stations_raw, services_raw = extracted_data
    disruptions_exploded = explode_row(disruptions_raw, "rdt_station_codes")
