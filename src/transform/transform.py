import pandas as pd

from src.logger import setup_logger
from src.transform.utils import explode_row, merge_dataframes

logger = setup_logger("transform", "transform.log")


def transform(extracted_data: list[pd.DataFrame]):
    logger.info("Starting data transformation")
    disruptions_raw, stations_raw, services_raw = extracted_data
    disruptions_exploded = explode_row(disruptions_raw, "rdt_station_codes")
    disruptions_merged = merge_dataframes(
        disruptions_exploded, stations_raw, "rdt_station_codes", "code"
    )
    services_merged = merge_dataframes(
        services_raw, stations_raw, "Stop:Station code", "code"
    )
