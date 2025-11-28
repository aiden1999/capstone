import gzip
import os
import shutil

import requests

from src.logger import setup_logger

SERVICES_GZIP_URL = (
    "https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz"
)

logger = setup_logger(__name__, "extract.log")


def check_data_sources(dir_path: str, csv_file: str, gzip_file: str):
    logger.info("Checking data sources...")
    if not check_file_exists(dir_path, csv_file):
        gzip_file_path = os.path.join(dir_path, gzip_file)
        if not check_file_exists(dir_path, gzip_file):
            download_file(SERVICES_GZIP_URL, gzip_file_path)
        csv_file_path = os.path.join(dir_path, csv_file)
        extract_file(gzip_file_path, csv_file_path)


def check_file_exists(dir_path: str, file: str) -> bool:
    path = os.path.join(dir_path, file)
    return os.path.isfile(path)


def download_file(url: str, output_path: str):
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
    logger.info(f"Decompressing {input_path}")
    try:
        with gzip.open(input_path, "rb") as file_in:
            with open(output_path, "wb") as file_out:
                shutil.copyfileobj(file_in, file_out)
        logger.info(f"Extracted {output_path}")
    except Exception as e:
        logger.error(f"Decompression failed: {e}")
        raise
