"""Checking that parquet files are ready for extraction.

Checks that the needed parquet files exists, if not orchestrate their download and/or extraction.
"""

import gzip
import os
import re
import shutil

import polars as pl
import requests

from src.logger import setup_logger

logger = setup_logger(__name__, "extract.log")


def check_data_sources(dir_path: str, file: dict):
    """Checks if a file exists and orchestrates downloading and/or
    decompressing if required.

    Args:
        dir_path: String representing the directory path of the raw data.
        file: Dictionary representing the file to check.
    """
    logger.info("Checking data sources...")
    if not check_file_exists(dir_path, file["file_name"]):
        output_path = os.path.join(dir_path, file["download_file"])
        download_file(file["url"], output_path)
    if get_file_type(dir_path, file["file_name"]) == "gz":
        extract_file(dir_path, file["download_file"])
    if get_file_type(dir_path, file["file_name"]) != "parquet":
        convert_to_parquet(dir_path, file["file_name"])


def check_file_exists(dir_path: str, file: str) -> bool:
    """Checks if a specified file path exists.

    Args:
        dir_path: String representing the directory path to check.
        file: String representing the file name to check.

    Returns:
        Boolean representing if the file exists or not: True if it exists,
            False otherwise.
    """
    logger.info(f"Checking if {dir_path}/{file} exists")
    try:
        files_in_dir = os.listdir(dir_path)
        file_regex = re.compile(re.escape(file) + r".*")
        matches = list(filter(file_regex.search, files_in_dir))
        return len(matches) > 0
    except Exception as e:
        logger.error(f"Error finding file: {e}")
        return False


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
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise


def get_file_type(dir_path: str, file: str) -> str:
    """Get the extension of a file.

    Args:
        dir_path: String representing the directory path of the file.
        file: String representing the name of the file.

    Returns:
        The file extension as a sting.
    """
    files_in_dir = os.listdir(dir_path)
    file_regex = re.compile(re.escape(file) + r".*")
    matches = list(filter(file_regex.search, files_in_dir))
    file_types = []
    for match in matches:
        split_file = match.split(".")
        file_types.append(split_file[-1])
    if "parquet" in file_types:
        return "parquet"
    elif "csv" in file_types:
        return "csv"
    else:
        return "gz"


def extract_file(dir_path: str, file: str):
    """Decompressing a file compressed with the gzip format.

    Args:
        dir_path: String representing the directory path of the compressed file.
        file: String representing the file to be decompressed.
    """
    logger.info(f"Decompressing {file}")
    input_path = os.path.join(dir_path, file)
    output_path = os.path.join(dir_path, file[0:-3])  # remove ".gz" from name
    try:
        with gzip.open(input_path, "rb") as file_in:
            with open(output_path, "wb") as file_out:
                shutil.copyfileobj(file_in, file_out)
    except Exception as e:
        logger.error(f"Decompression failed: {e}")
        raise


def convert_to_parquet(dir_path: str, file: str):
    """Convert a CSV file to Parquet.

    Args:
        dir_path: String representing the directory path of the file.
        file: String representing the file to de converted.
    """
    input_file = file + ".csv"
    input_path = os.path.join(dir_path, input_file)
    output_file = file + ".parquet"
    output_path = os.path.join(dir_path, output_file)
    df = pl.scan_csv(input_path)
    df.sink_parquet(output_path)
