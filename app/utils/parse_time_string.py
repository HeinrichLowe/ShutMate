import re


def parse_time_string(time_str: str) -> int | None:
    """
    Convert a time string like "1H 30M" into total seconds.

    Args:
        time_str (str): The time string to parse.

    Returns:
        int or None: Total seconds represented by the time string, or None if the input is invalid.
    """

    if time_str == "Select the timer":
        return None

    hours = 0
    minutes = 0

    match = re.findall(r"(\d+)\s*H", time_str)
    if match:
        hours = int(match[0])

    match = re.findall(r"(\d+)\s*M", time_str)
    if match:
        minutes = int(match[-1]) if len(match) > 1 else int(match[0])

    return (hours * 3600) + (minutes * 60)
