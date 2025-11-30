import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def merge_disruptions_with_services(
    disruptions_df: pd.DataFrame, services_df: pd.DataFrame
) -> pd.DataFrame:
    disruptions_clean = disruptions_df.dropna()
    merged = merge(disruptions_clean, services_df)
    return merged


# don't think I need this, maybe delete later
def drop_non_ns_services(services: pd.DataFrame) -> pd.DataFrame:
    logger.info("Removing non-NS services")
    try:
        ns_mask = services["Service:Company"].isin(["NS"])
        ns_services = services[ns_mask]
        ns_services.reset_index(drop=True, inplace=True)
        logger.info("Removed non-NS services successfully")
        return ns_services
    except Exception as e:
        logger.error(f"Error with removing non-NS services: {e}")
        raise


def merge(disruptions: pd.DataFrame, services: pd.DataFrame) -> pd.DataFrame:
    merge_result = services.merge(disruptions, on="code", how="left")
    arrival_overlap = (
        merge_result["start_time"] <= merge_result["Stop:Arrival time"]
    ) & (merge_result["Stop:Arrival time"] <= merge_result["end_time"])
    departure_overlap = (
        merge_result["start_time"] <= merge_result["Stop:Departure time"]
    ) & (merge_result["Stop:Departure Time"] <= merge_result["end_time"])
    valid_services = (arrival_overlap | departure_overlap) | merged["rtd_id"].isna()
    merge_result = merge_result[valid_services]
    merge_result["was_disrupted"] = merge_result["rtd_id"].notna()
    merge_result.reset_index(drop=True, inplace=True)
    return merge_result
