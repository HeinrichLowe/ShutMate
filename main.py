import sys

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QApplication

# pylint: enable=no-name-in-module
from app.ui.main_window.main_window import main_window

# --- Aplication PyQt6 ---
app = QApplication(sys.argv)
window = main_window()
window.show()
sys.exit(app.exec())
