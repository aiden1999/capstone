"""Utilities for logging."""

import logging
import os
import sys
from pathlib import Path


def setup_logger(
    name: str, log_file: str, level: int = logging.DEBUG
) -> logging.Logger:
    """Sets up the logger for use elsewhere.

    Args:
        name: String representing the name of the logger.
        log_file: String representing the file for the logger's logs to be
            recorded.
        level: Level of logging needed.

    Returns:
        Logger object.
    """
    log_directory = ensure_log_directory("logs")
    if log_directory is None:
        log_directory = Path("logs")
    else:
        log_directory = Path(log_directory)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        file_handler, console_handler = create_handlers(log_directory, log_file, level)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger


def ensure_log_directory(path: str):
    log_directory = os.makedirs(path, exist_ok=True)
    return log_directory


def create_handlers(log_directory, log_file, level):
    log_format = "%(asctime)s %(name)s %(levelname)s %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_format, datefmt=date_format)
    file_handler = logging.FileHandler(log_directory / log_file)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    return file_handler, console_handler
