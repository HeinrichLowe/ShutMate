import os
import sys
import logging


def resource_path(relative_path: str) -> str:
    """
    Returns the absolute path to a resource file given its relative path.

    Args:
        relative_path (str): The relative path to the resource file.

    Returns:
        str: The absolute path to the resource file.
    """

    try:
        base_path = getattr(sys, "_MEIPASS", None)
        if base_path is None:
            base_path = os.path.abspath(".")

    except Exception as err:  # pylint: disable=broad-exception-caught
        logging.exception("Error getting base path: %s", err)
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
