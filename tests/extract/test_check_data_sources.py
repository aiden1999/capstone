import pytest
import os
from src.extract.check_data_sources import (
    check_file_exists,
    convert_to_parquet,
    download_file,
    extract_file,
    get_file_type,
)


def test_check_file_exists_returns_true():
    existing_file = "sample-1"
    existing_dir = "data/test"
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
    url = "https://getsamplefiles.com/download/txt/sample-2.txt"
    output_dir = "data/test"
    output_file = "sample-2.txt"
    output_path = os.path.join(output_dir, output_file)
    download_file(url, output_path)
    assert os.path.exists(output_path)


def test_get_file_type_returns_parquet():
    dir_path = "data/raw"
    file = "stations-2023-09"
    expected_file_type = "parquet"
    actual_file_type = get_file_type(dir_path, file)
    assert expected_file_type == actual_file_type


def test_get_file_type_returns_csv():
    dir_path = "data/test"
    file = "sample-3"
    expected_file_type = "csv"
    actual_file_type = get_file_type(dir_path, file)
    assert expected_file_type == actual_file_type


def test_get_file_type_returns_gz():
    dir_path = "data/test"
    file = "sample-4"
    expected_file_type = "gz"
    actual_file_type = get_file_type(dir_path, file)
    assert expected_file_type == actual_file_type


def test_extract_file_works():
    dir = "data/test"
    input_file = "sample-5.gz"
    output_file = "sample-5"
    output_path = os.path.join(dir, output_file)
    extract_file(dir, input_file)
    assert os.path.exists(output_path)


def test_extract_file_raises_exception():
    dir = "data/test"
    input_file = "sample-2.gz"
    with pytest.raises(Exception):
        extract_file(dir, input_file)


def test_convert_to_parquet_works():
    dir = "data/test"
    input_file = "sample-6"
    output_file = "sample-6.parquet"
    output_path = os.path.join(dir, output_file)
    convert_to_parquet(dir, input_file)
    assert os.path.exists(output_path)


def test_convert_to_parquet_raises_exception():
    dir = "data/test"
    file = "not_real"
    with pytest.raises(Exception):
        convert_to_parquet(dir, file)
