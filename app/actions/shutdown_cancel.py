import os
from app.ui.show_notification.show_notification import ShowNotification as SN
from app.utils.run_command_no_window import run_command_no_window


def shutdown_cancel(main_window):
    """
    Cancels any scheduled system shutdown.

    Args:
        main_window (QWidget): The parent window for the notification
    """

    if os.name == "nt":
        run_command_no_window("shutdown /a")
    else:
        run_command_no_window("shutdown -c")

    notification = SN(main_window, "Shutdown canceled.")
    notification.exec()
