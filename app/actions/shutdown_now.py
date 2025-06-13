import os
from app.utils.run_command_no_window import run_command_no_window


def shutdown_now() -> None:
    """
    Turn off the computer immediately.
    """

    if os.name == "nt":
        run_command_no_window("shutdown /s /t 0")
    else:
        run_command_no_window("shudown -h now")
