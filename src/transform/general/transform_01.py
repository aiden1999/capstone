import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def transform_01(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming for 01")
    num_services = df["Service:RDT-ID"].nunique()
    transformed_df = pd.DataFrame({"total_planned_services": [num_services]})
    logger.info("Successed transformed for 01")
    return transformed_df
