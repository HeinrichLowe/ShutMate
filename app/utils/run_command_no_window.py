import os
import subprocess


def run_command_no_window(command: str):
    """
    Run a command without opening a terminal window.
    """

    if os.name == "nt":
        # No terminal window on Windows
        subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
    else:
        subprocess.Popen(command, shell=True)
