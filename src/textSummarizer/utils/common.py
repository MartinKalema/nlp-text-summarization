import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents wrapped in a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: Any other unexpected error that occurs during file reading.

    Returns:
        ConfigBox: A ConfigBox containing the contents of the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories specified in the list.

    Args:
        path_to_directories (list): A list of directory paths to be created.
        verbose (bool, optional): If True, log messages will be displayed for each directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in kilobytes.

    Args:
        path (Path): The path to the file whose size is required.

    Returns:
        str: A string representing the size of the file in kilobytes, rounded to the nearest whole number.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"