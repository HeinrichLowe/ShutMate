import sys
import os
import re
from app.utils.resource_path import resource_path


def css_loader(file_path: str) -> str:
    """
    This function reads a CSS file, processes any relative URLs within it,
    and returns the content as a string.

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

    def repl(match):
        rel_path = match.group(1).replace("\\", "/")

        if not (rel_path.startswith("http") or rel_path.startswith("data:")):
            abs_path = resource_path(rel_path).replace("\\", "/")
            return f"url({abs_path})"

        return match.group(0)

    css_content = re.sub(r"url\(([^)]+)\)", repl, css_content)

    return css_content
