from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt


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
        layout = QVBoxLayout()
        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet(
            "background-color: #0078D7; color: white; padding: 5px none;"
        )
        btn_ok.clicked.connect(self.accept)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_ok)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)
