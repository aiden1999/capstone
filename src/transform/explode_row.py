import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def explode_row(df: pd.DataFrame, column: str) -> pd.DataFrame:
    logger.info(f"Exploding {df} on column {column}")
    try:
        df[column] = df[column].str.split(",")
        df_exploded = df.explode(column).reset_index(drop=True)
        logger.info("Explode succeeded")
        return df_exploded
    except Exception as e:
        logger.error(f"Explode failed: {e}")
        raise
