import subprocess
from src.logger import setup_logger


logger = setup_logger("Testing", "tests.log")


def main():
    logger.info("Started linting")
    subprocess.run(["ruff", "check"])
    logger.info("Finished linting")
    logger.info("Running tests")
    subprocess.run(["pytest", "--verbose", "--cov"])
    logger.info("Finished running tests")


if __name__ == "__main__":
    main()
