from src.extract.extract import extract_data
from src.logger import setup_logger


def main():
    logger = setup_logger("etl_pipeline", "etl_pipeline.log")
    try:
        logger.info("Starting ETL pipeline")
        logger.info("Starting extraction phase")
        extracted_data = extract_data()
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")


if __name__ == "__main__":
    main()
