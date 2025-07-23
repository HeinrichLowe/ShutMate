from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from app.actions import shutdown_now
from app.utils.css_loader import css_loader
from app.utils.resource_path import resource_path

SC_CSS = css_loader(resource_path("app/assets/css/shutdown_confirmation.css"))


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
        self.setStyleSheet(SC_CSS)
        layout = QVBoxLayout()
        label = QLabel("Are you sure you want to shut down the computer now?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_yes = QPushButton("Yes")
        btn_yes.setObjectName("shutdownConfirmationYesButton")
        btn_yes.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_yes.clicked.connect(self._on_yes_clicked)

        btn_no = QPushButton("No")
        btn_no.setObjectName("shutdownConfirmationNoButton")
        btn_no.setCursor(Qt.CursorShape.PointingHandCursor)
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
