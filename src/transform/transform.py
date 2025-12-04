"""Transform phase for the ETL pipeline.

Called in run_etl.
"""

import pandas as pd

from src.constants import (
    # DPCC_COLUMNS,
    GENERAL_COLUMNS,
    INTERNATIONAL_COUNTRIES,
    # STATIONS_COLUMNS,
)
from src.logger import setup_logger
from src.transform.general.transform_general import transform_general
from src.transform.utils import (
    keep_columns,
    # explode_row,
    merge_dataframes,
)

logger = setup_logger("transform", "transform.log")


def transform_data(extracted_data: list[pd.DataFrame]) -> list[list[pd.DataFrame]]:
    """Orchestrated the transformation of data from DataFrames.

    Args:
        extracted_data: List of DataFrames of the data extracted from CSVs.

    Returns:
        The transformed DataFrames.
    """
    logger.info("Starting data transformation")
    disruptions_raw, stations_raw, services_raw = extracted_data

    # INFO: needed for disruptions 

    # disruptions_exploded = explode_row(disruptions_raw, "rdt_station_codes")
    # disruptions_merged = merge_dataframes(
    #     disruptions_exploded, stations_raw, "rdt_station_codes", "code"
    # )
    services_merged = merge_dataframes(
        services_raw, stations_raw, "Stop:Station code", "code"
    )

    # INFO: needed for disruptions 

    # logger.info("Removing international data from disruptions")
    # domestic_disruptions = remove_international_data(disruptions_merged)
    logger.info("Removing international data from services")
    domestic_services = remove_international_data(services_merged)
    logger.info("Dropping columns")
    general_df = keep_columns(domestic_services, GENERAL_COLUMNS)

    # INFO: for future work 

    # stations_df = drop_columns(stations_df, STATIONS_COLUMNS)
    # dpcc_df = drop_columns(dpcc_df, DPCC_COLUMNS)
    # TODO: drop_columns for disruptions

    general_dfs = transform_general(general_df)
    return [general_dfs]


def remove_international_data(df: pd.DataFrame) -> pd.DataFrame:
    """Removes international data from a DataFrame.

    Makes a DataFrame of the service IDs that have a stop in an international
    country, and removes the rows that have that service ID, hence also deleting
    international sevices that have stops in the Netherlands.

    Args:
        df: DataFrame with service data.

    Returns:
        DataFrame without international services.
    """
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
