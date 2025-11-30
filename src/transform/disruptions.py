import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def merge_disruptions_with_services(
    disruptions_pd: pd.DataFrame, services_pd: pd.DataFrame
) -> pd.DataFrame:
    # drop non ns services from services
    ns_services = drop_non_ns_services(services_pd)
    pass


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
