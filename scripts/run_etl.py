from src.constants import OUTPUT_PATH
from src.extract.extract import extract_data
from src.load.load import load_data
from src.logger import setup_logger
from src.transform.transform import transform_data


def main():
    logger = setup_logger("etl_pipeline", "etl_pipeline.log")
    try:
        logger.info("Starting ETL pipeline")
        logger.info("Starting extraction phase")
        extracted_data = extract_data()
        logger.info("Completed extraction phase")
        logger.info("Starting transform phase")
        transformed_data = transform_data(extracted_data)
        logger.info("Completed transform phase")
        logger.info("Starting load phase")
        load_data(transformed_data, OUTPUT_PATH)
        logger.info("Completed load phase")
        logger.info("ETL pipeline completed sucessfully")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")


if __name__ == "__main__":
    main()
