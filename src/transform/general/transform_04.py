import polars as pl

from src.logger import setup_logger
from src.transform.constants import VIS_04_COLUMNS
from src.transform.utils import keep_columns

logger = setup_logger(__name__, "transform.log")


def transform_04(df: pl.DataFrame) -> pl.DataFrame:
    """Transforms data needed for visualisation 04.

    Args:
        df: DataFrame for general statistics.

    Returns:
        Transformed DataFrame.
    """
    logger.info("Transforming for 04")
    df = keep_columns(df, VIS_04_COLUMNS)
    start_df = df.select(
        pl.col("Service:RDT-ID"),
        pl.col("Stop:Station name").alias("station_start"),
        pl.col("geo_lat").alias("lat_start"),
        pl.col("geo_lng").alias("lng_start"),
        pl.col("Stop:Departure time").cast(pl.Datetime),
        pl.col("Stop:Departure delay"),
    ).filter(df["Stop:Arrival time"].is_null())
    end_df = df.select(
        pl.col("Service:RDT-ID"),
        pl.col("Stop:Station name").alias("station_end"),
        pl.col("geo_lat").alias("lat_end"),
        pl.col("geo_lng").alias("lng_end"),
        pl.col("Stop:Arrival time").cast(pl.Datetime),
        pl.col("Stop:Arrival delay"),
    ).filter(df["Stop:Departure time"].is_null())
    joined_df = start_df.join(end_df, "Service:RDT-ID")
    joined_df = joined_df.with_columns(
        (
            (pl.col("Stop:Departure delay") > 0) | (pl.col("Stop:Arrival delay") > 0)
        ).alias("was_delayed"),
        (
            pl.duration(
                minutes=(pl.col("Stop:Arrival delay") - pl.col("Stop:Departure delay"))
            )
        ).alias("total_delay"),
        (pl.col("Stop:Arrival time") - pl.col("Stop:Departure time")).alias(
            "journey_time"
        ),
    )
    joined_df = joined_df.with_columns(
        (pl.col("journey_time") + pl.col("total_delay")).alias(
            "journey_time_with_delays"
        )
    )
    joined_df = joined_df.with_columns(
        pl.col("journey_time").dt.total_minutes(),
        pl.col("journey_time_with_delays").dt.total_minutes(),
    ).drop(
        [
            "Stop:Departure time",
            "Stop:Departure delay",
            "Stop:Arrival time",
            "Stop:Arrival delay",
            "total_delay",
        ]
    )
    return joined_df
