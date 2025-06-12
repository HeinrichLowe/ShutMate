import os

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QComboBox

# pylint: enable=no-name-in-module
from app.ui.show_notification.show_notification import show_notification
from app.utils.parse_time_string import parse_time_string


def schedule_shutdown(main_window, combo_box: QComboBox) -> None:
    """
    Schedule a shutdown based on the selected time from the combo box.
    """

    selected_time = combo_box.currentText()
    total_seconds = parse_time_string(selected_time)
    if total_seconds is None:
        show_notification(main_window, "Please select a valid time!", "Error")
        return

    if os.name == "nt":
        os.system(f"shutdown /s /t {total_seconds}")
    else:
        minutes = max(1, total_seconds // 60)
        os.system(f"shutdown -h +{minutes}")

    show_notification(main_window, f"Desligamento programado para {selected_time}.")
