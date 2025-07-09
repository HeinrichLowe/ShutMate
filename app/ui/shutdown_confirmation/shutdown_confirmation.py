from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from app.actions import shutdown_now


class ShutdownConfirmation(QDialog):
    """
    Dialog to confirm the shutdown action with the user.

    This dialog asks the user to confirm if they want to shut down the computer now.

    Args:
        parent (QWidget, optional): Parent widget. Defaults to None.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Shutdown")
        layout = QVBoxLayout()
        label = QLabel("Are you sure you want to shut down the computer now?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_yes = QPushButton("Yes")
        btn_yes.setStyleSheet(
            "background-color: #E74C3C; color: white; padding: 5px none;"
        )
        btn_yes.clicked.connect(self._on_yes_clicked)

        btn_no = QPushButton("No")
        btn_no.setStyleSheet(
            "background-color: #0078D7; color: white; padding: 5px none;"
        )
        btn_no.clicked.connect(self.reject)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_yes)
        btn_layout.addWidget(btn_no)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def _on_yes_clicked(self):
        shutdown_now()
        self.accept()
