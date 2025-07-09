import sys
from PyQt6.QtWidgets import QApplication
from app.ui.main_window.main_window import MainWindow

# --- Aplication PyQt6 ---
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
