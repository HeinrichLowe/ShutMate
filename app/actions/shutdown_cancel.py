import os
from app.ui.show_notification.show_notification import show_notification
from app.utils.run_command_no_window import run_command_no_window


def shutdown_cancel(main_window):
    """
    Cancel any scheduled shutdown.
    """

    if os.name == "nt":
        run_command_no_window("shutdown /a")
    else:
        run_command_no_window("shutdown -c")

    show_notification(main_window, "Shutdown cancelled.")
