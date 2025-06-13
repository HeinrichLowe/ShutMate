import sys
import os


def css_loader(file_path: str) -> str:
    """
    Load a CSS file and return its content as a string.

    Args:
        file_path (str): Path to the CSS file.

    Returns:
        str: Content of the CSS file as a string.
    """

    if not os.path.exists(file_path):
        print(f"CSS file not found: {file_path}", file=sys.stderr)
        return ""

    with open(file_path, "r", encoding="utf-8") as file:
        css_content = file.read()

    return css_content
