import os
import subprocess


def run_command_no_window(command: str) -> None:
    """
    Runs a command without opening a terminal window.

    Args:
        command (str): The command to run
    """

    if os.name == "nt":
        # No terminal window on Windows
        with subprocess.Popen(
            command, creationflags=subprocess.CREATE_NO_WINDOW, shell=True
        ):
            pass
    else:
        with subprocess.Popen(command, shell=True):
            pass
