import re


def parse_time_string(time_str: str) -> int | None:
    """
    Convert a time string like "01:30" into total seconds.

    Args:
        time_str (str): The time string to parse.

    Returns:
        int or None: Total seconds represented by the time string, or None if the input is invalid.
    """

    if time_str == "Select the timer":
        return None

    match = re.match(r"^(\d{2}):(\d{2})$", time_str)
    if not match:
        return None

    hours = int(match.group(1))
    minutes = int(match.group(2))

    return (hours * 3600) + (minutes * 60)
