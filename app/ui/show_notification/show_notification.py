from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from app.utils.css_loader import css_loader
from app.utils.resource_path import resource_path

SN_CSS = css_loader(resource_path("app/assets/css/show_notification.css"))


class ShowNotification(QDialog):
    """
    Show a notification message box.

    Args:
        parent (QWidget, optional): Parent widget. Defaults to None.
        message (str): The message to display.
        title (str): The title of the message box.

    Returns:
        None: Displays a message box with the given title and message.
    """

    def __init__(self, parent, message: str, title: str = "Notification"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setStyleSheet(SN_CSS)
        layout = QVBoxLayout()
        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_ok = QPushButton("OK")
        btn_ok.setObjectName("showNotificationOkButton")
        btn_ok.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_ok.clicked.connect(self.accept)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_ok)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)
