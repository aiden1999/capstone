import gzip
import os

import requests
import shutil

SERVICES_GZIP_URL = (
    "https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz"
)


def check_data_sources(dir_path: str, csv_file: str, gzip_file: str):
    if not check_file_exists(dir_path, csv_file):
        gzip_file_path = os.path.join(dir_path, gzip_file)
        if not check_file_exists(dir_path, gzip_file):
            download_file(SERVICES_GZIP_URL, gzip_file_path)
        csv_file_path = os.path.join(dir_path, csv_file)
        extract_file(gzip_file_path, csv_file_path)


def check_file_exists(dir_path: str, file: str) -> bool:
    path = os.path.join(dir_path, file)
    return os.path.isfile(path)


def download_file(url: str, output_path):
    print("downloading file")  # TODO: log
    try:
        response = requests.get(url, stream=True)
        print(response.status_code)  # TEST: also change to log
        response.raise_for_status()
        chunk_size = 1024 * 1024  # 1 MB chunk size
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
        # TODO: log file downloaded
    except Exception as e:
        raise Exception(f"Error: {e}")


def extract_file(input_path, output_path):
    print("extracting file")  # TODO: log
    try:
        with gzip.open(input_path, "rb") as file_in:
            with open(output_path, "wb") as file_out:
                shutil.copyfileobj(file_in, file_out)
        # TODO: log file extracted
    except Exception as e:
        raise Exception(f"Error: {e}")
