import pandas as pd

from src.logger import setup_logger

logger = setup_logger(__name__, "transform.log")


def explode_row(df: pd.DataFrame, column: str) -> pd.DataFrame:
    logger.info(f"Exploding dataframe on column {column}")
    try:
        df[column] = df[column].str.split(",")
        df_exploded = df.explode(column)
        df_exploded[column] = df_exploded[column].str.strip()
        df_exploded = df_exploded.reset_index(drop=True)
        logger.info("Explode succeeded")
        return df_exploded
    except Exception as e:
        logger.error(f"Explode failed: {e}")
        raise


def merge_dataframes(
    df_1: pd.DataFrame, df_2: pd.DataFrame, col_1: str, col_2: str
) -> pd.DataFrame:
    logger.info("Merging...")
    try:
        merged_df = df_1.merge(df_2, left_on=col_1, right_on=col_2)
        logger.info("Merge succeeded")
        return merged_df
    except Exception as e:
        logger.error(f"Merge failed: {e}")
        raise


def make_df_copy(df: pd.DataFrame) -> pd.DataFrame:
    copied_df = df.copy()
    return copied_df
