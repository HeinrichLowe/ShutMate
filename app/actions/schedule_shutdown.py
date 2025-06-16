import os
from PyQt6.QtWidgets import QComboBox
from app.ui.show_notification.show_notification import show_notification
from app.utils.parse_time_string import parse_time_string
from app.utils.run_command_no_window import run_command_no_window


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
        run_command_no_window(f"shutdown /s /t {total_seconds}")
    else:
        minutes = max(1, total_seconds // 60)
        run_command_no_window(f"shutdown -h +{minutes}")

    show_notification(main_window, f"Scheduled shutdown for {selected_time}.")
