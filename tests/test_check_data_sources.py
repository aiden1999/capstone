import pytest
import os
from src.extract.check_data_sources import (
    check_file_exists,
    download_file,
    extract_file,
)


def test_check_file_exists_returns_true():
    existing_file = "stations-2023-09.csv"
    existing_dir = "data/raw"
    file_exists = check_file_exists(existing_dir, existing_file)
    assert file_exists


def test_check_file_exists_returns_false():
    missing_file = "something.txt"
    missing_dir = "a/file/path"
    file_exists = check_file_exists(missing_dir, missing_file)
    assert not file_exists


def test_download_file_raises_exception():
    url = "https://google.com/404"
    output_dir = "data/test"
    output_file = "non_existent.txt"
    output_path = os.path.join(output_dir, output_file)
    with pytest.raises(Exception):
        download_file(url, output_path)


def test_download_file_works():
    url = "https://getsamplefiles.com/download/gzip/sample-1.gz"
    output_dir = "data/test"
    output_file = "sample-1.gz"
    output_path = os.path.join(output_dir, output_file)
    download_file(url, output_path)
    assert os.path.exists(output_path)


def test_extract_file_works():
    dir = "data/test"
    input_file = "sample-1.gz"
    output_file = "sample-1"
    input_path = os.path.join(dir, input_file)
    output_path = os.path.join(dir, output_file)
    extract_file(input_path, output_path)
    assert os.path.exists(output_path)


def test_extract_file_raises_exception():
    dir = "data/test"
    input_file = "sample-2.gz"
    output_file = "sample-2"
    input_path = os.path.join(dir, input_file)
    output_path = os.path.join(dir, output_file)
    with pytest.raises(Exception):
        extract_file(input_path, output_path)
