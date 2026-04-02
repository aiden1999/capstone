"""Script to run the ETL pipeline."""

from src.constants import OUTPUT_PATH
from src.extract.extract import extract_data
from src.load.load import load_data
from src.logger import setup_logger
from src.transform.transform import transform_data


def main():
    """Calls each phase of the ETL pipeline and logs it."""
    logger = setup_logger("etl_pipeline", "etl_pipeline.log")
    try:
        logger.info("Starting ETL pipeline")
        logger.info("Starting extraction phase")
        extracted_data = extract_data()
        logger.info("Starting transform phase")
        transformed_data = transform_data(extracted_data)
        logger.info("Starting load phase")
        load_data(transformed_data, OUTPUT_PATH)
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")


if __name__ == "__main__":
    main()
