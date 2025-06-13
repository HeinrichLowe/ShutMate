from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from app.actions import shutdown_now


def shutdown_confirmation(main_window) -> None:
    """
    Confirm the shutdown action with the user.
    """

    dialog = QDialog(main_window)
    dialog.setWindowTitle("Confirm Shutdown")
    layout = QVBoxLayout()
    label = QLabel("Are you sure you want to shut down the computer now?")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label)

    btn_yes = QPushButton("Yes")
    btn_yes.setStyleSheet("background-color: #0078D7; color: white; padding: 5px none;")
    btn_yes.clicked.connect(shutdown_now)

    btn_no = QPushButton("No")
    btn_no.setStyleSheet("background-color: #E74C3C; color: white; padding: 5px none;")
    btn_no.clicked.connect(dialog.reject)

    # Centraliza os botões
    btn_layout = QHBoxLayout()
    btn_layout.addStretch()
    btn_layout.addWidget(btn_yes)
    btn_layout.addWidget(btn_no)
    btn_layout.addStretch()
    layout.addLayout(btn_layout)

    dialog.setLayout(layout)
    dialog.exec()
