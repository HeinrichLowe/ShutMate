import os
from app.ui.show_notification.show_notification import show_notification


def shutdown_cancel(main_window):
    """
    Cancel any scheduled shutdown.
    """

    if os.name == "nt":
        os.system("shutdown /a")
    else:
        os.system("shutdown -c")

    show_notification(main_window, "Desligamento cancelado.")
