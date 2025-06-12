import os
from app.ui.show_notification.show_notification import show_notification


def shutdown_now(main_window) -> None:
    """
    Turn off the computer immediately.
    """

    if os.name == "nt":
        # os.system("shutdown /s /t 0")
        show_notification(main_window, "Desligando o Windows agora...")
    else:
        # os.system("shudown -h now")
        show_notification(main_window, "Desligando o Linux agora...")
