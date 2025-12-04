"""Checking that services-2024.csv is ready for extraction.

Both services-2024.csv and its compressed version (services-2024.csv.gz) are
too large to be stored on GitHub, so the file(s) may need to be downloaded
and/or decompressed.
"""

import gzip
import os
import shutil

import requests

from src.constants import SERVICES_GZIP_URL
from src.logger import setup_logger


logger = setup_logger(__name__, "extract.log")


def check_data_sources(dir_path: str, csv_file: str, gzip_file: str):
    """Checks if services-2024.csv exists and orchestrates downloading and/or
    decompressing if required.

    Args:
        dir_path: String representing the directory path of the raw data.
        csv_file: String representing the csv file name to check.
        gzip_file: String representing the gzip file name to check.
    """
    logger.info("Checking data sources...")
    if not check_file_exists(dir_path, csv_file):
        gzip_file_path = os.path.join(dir_path, gzip_file)
        if not check_file_exists(dir_path, gzip_file):
            download_file(SERVICES_GZIP_URL, gzip_file_path)
        csv_file_path = os.path.join(dir_path, csv_file)
        extract_file(gzip_file_path, csv_file_path)


def check_file_exists(dir_path: str, file: str) -> bool:
    """Checks if a specified file path exists.

    Args:
        dir_path: String representing the directory path to check.
        file: String representing the file name to check.

    Returns:
        Boolean representing if the file exists or not: True if it exists,
            False otherwise.
    """
    path = os.path.join(dir_path, file)
    return os.path.isfile(path)


def download_file(url: str, output_path: str):
    """Downloads a file from the specified url.

    Args:
        url: String representing the url of the file.
        output_path: String representing the path of the downloaded file.
    """
    logger.info(f"Downloading file from {url}")
    try:
        response = requests.get(url, stream=True)
        logger.info(f"Got response: {response.status_code}")
        response.raise_for_status()
        chunk_size = 1024 * 1024  # 1 MB chunk size
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
        logger.info("File finished downloading.")
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise


def extract_file(input_path: str, output_path: str):
    """Decompressing a file compressed with the gzip format.

    Args:
        input_path: String representing the path of the compressed file.
        output_path: String representing the path of the decompressed file.
    """
    logger.info(f"Decompressing {input_path}")
    try:
        with gzip.open(input_path, "rb") as file_in:
            with open(output_path, "wb") as file_out:
                shutil.copyfileobj(file_in, file_out)
        logger.info(f"Extracted {output_path}")
    except Exception as e:
        logger.error(f"Decompression failed: {e}")
        raise
