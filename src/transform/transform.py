import pandas as pd

from src.constants import (
    DPCC_COLUMNS,
    GENERAL_COLUMNS,
    INTERNATIONAL_COUNTRIES,
    STATIONS_COLUMNS,
)
from src.logger import setup_logger
from src.transform.disruptions import merge_disruptions_with_services
from src.transform.utils import (
    drop_columns,
    explode_row,
    make_df_copy,
    merge_dataframes,
)

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
    logger.info("Merging disruptions with services")
    disruptions_df = merge_disruptions_with_services(
        domestic_disruptions, domestic_services
    )
    logger.info("Creating dataframe copies")
    general_df = make_df_copy(domestic_services)
    stations_df = make_df_copy(domestic_services)
    dpcc_df = make_df_copy(domestic_services)
    logger.info("Dropping columns")
    general_df = drop_columns(general_df, GENERAL_COLUMNS)
    stations_df = drop_columns(stations_df, STATIONS_COLUMNS)
    dpcc_df = drop_columns(dpcc_df, DPCC_COLUMNS)
    print(disruptions_df)
    # TODO: drop_columns for disruptions


def remove_international_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Removing international data")
    try:
        country_mask = df["country"].isin(INTERNATIONAL_COUNTRIES)
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
