import pandas as pd

from src.logger import setup_logger
from src.transform.utils import explode_row, merge_dataframes

logger = setup_logger("transform", "transform.log")


def transform_data(extracted_data: list[pd.DataFrame]):
    logger.info("Starting data transformation")
    disruptions_raw, stations_raw, services_raw = extracted_data
    disruptions_exploded = explode_row(disruptions_raw, "rdt_station_codes")
    disruptions_merged = merge_dataframes(
        disruptions_exploded, stations_raw, "rdt_station_codes", "code"
    )
    services_merged = merge_dataframes(
        services_raw, stations_raw, "Stop:Station code", "code"
    )
    logger.info("Removing international data from disruptions")
    domestic_disruptions = remove_international_data(disruptions_merged)
    logger.info("Removing international data from services")
    domestic_services = remove_international_data(services_merged)


def remove_international_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Removing international data")
    try:
        international_countries = [
            "A",  # Austria
            "B",  # Belgium
            "CH",  # Switzerland
            "D",  # Germany
            "DK",  # Denmark
            "F",  # France
            "GB",  # United Kingdom
            "I",  # Italy
            "S",  # Sweden
        ]
        country_mask = df["country"].isin(international_countries)
        international_df = df[country_mask]
        international_ids = international_df.iloc[:, 0].unique().tolist()
        id_mask = ~df.iloc[:, 0].isin(international_ids)
        domestic_df = df[id_mask]
        domestic_df.reset_index(drop=True, inplace=True)
        logger.info("Removed international data")
        return domestic_df
    except Exception as e:
        logger.error(f"Removing international data failed: {e}")
        raise
