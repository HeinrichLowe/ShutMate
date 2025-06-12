import sys
import re
import os

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QToolButton,  # Adicione esta linha
    QLabel,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
    QPushButton,
)
from PyQt6.QtCore import QSize, Qt  # Importar Qt para alinhamento e ícones
from PyQt6.QtGui import QIcon, QFont  # Para ícones e fontes (opcional)

# pylint: enable=no-name-in-module


# --- Functions ---
def shutdown_now() -> None:
    """
    Turn off the computer immediately.
    """

    if os.name == "nt":
        # os.system("shutdown /s /t 0")
        show_notification("Desligando o Windows agora...")
    else:
        # os.system("shudown -h now")
        show_notification("Desligando o Linux agora...")


def parse_time_string(time_str: str) -> int:
    """
    Convert a time string like "1H 30M" into total seconds.

    Args:
        time_str (str): The time string to parse.

    Returns:
        int: Total seconds represented by the time string.
    """

    if time_str == "Select the timer":
        return None

    hours = 0
    minutes = 0

    match = re.findall(r"(\d+)\s*H", time_str)
    if match:
        hours = int(match[0])

    match = re.findall(r"(\d+)\s*M", time_str)
    if match:
        minutes = int(match[-1]) if len(match) > 1 else int(match[0])

    return (hours * 3600) + (minutes * 60)


def schedule_shutdown():
    """
    Schedule a shutdown based on the selected time from the combo box.
    """

    selected_time = combo_box.currentText()
    total_seconds = parse_time_string(selected_time)
    if total_seconds is None:
        show_notification("Selecione um tempo válido!", "Erro")
        return

    if os.name == "nt":
        os.system(f"shutdown /s /t {total_seconds}")
    else:
        minutes = max(1, total_seconds // 60)
        os.system(f"shutdown -h +{minutes}")

    show_notification(f"Desligamento programado para {selected_time}.")


def shutdown_cancel():
    """
    Cancel any scheduled shutdown.
    """

    if os.name == "nt":
        os.system("shutdown /a")
    else:
        os.system("shutdown -c")

    show_notification("Desligamento cancelado.")


def shutdown_confirmation() -> None:
    """
    Confirm the shutdown action with the user.
    """

    dialog = QDialog(window)
    dialog.setWindowTitle("Confirm Shutdown")
    layout = QVBoxLayout()
    label = QLabel("Tem certeza que quer desligar o computador agora?")
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


def show_notification(message, title="Notification") -> None:
    """
    Show a notification message box.

    Args:
        message (str): The message to display.
        title (str): The title of the message box.

    Returns:
        None: Displays a message box with the given title and message.
    """

    dialog = QDialog(window)
    dialog.setWindowTitle(title)
    layout = QVBoxLayout()
    label = QLabel(message)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label)

    btn_ok = QPushButton("OK")
    btn_ok.setStyleSheet("background-color: #0078D7; color: white; padding: 5px none;")
    btn_ok.clicked.connect(dialog.accept)

    # Centraliza o botão
    btn_layout = QHBoxLayout()
    btn_layout.addStretch()
    btn_layout.addWidget(btn_ok)
    btn_layout.addStretch()
    layout.addLayout(btn_layout)

    dialog.setLayout(layout)
    dialog.exec()


def fechar_combo():
    """
    Close the combo box popup when an item is selected.
    """

    combo_box.hidePopup()


# --- Aplication PyQt6 ---
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Sleep")
window.setMinimumSize(QSize(800, 600))

# --- Widgets ---

# Label "Sleep in:"
label_sleep_in = QLabel("Sleep in:")
label_sleep_in.setFont(QFont("Segoe UI", 12))

# ComboBox (Dropdown)
combo_box = QComboBox()
combo_box.setMaxVisibleItems(10)
combo_box.addItems(
    [
        "Select the timer",  # Placeholder/primeira opção
        "30M",
        "1H",
        "1H 30M",
        "2H",
        "2H 30M",
        "3H",
        "3H 30M",
        "4H",
        "4H 30M",
        "5H",
        "5H 30M",
        "6H",
        "6H 30M",
        "7H",
        "7H 30M",
        "8H",
        "8H 30M",
        "9H",
        "9H 30M",
        "10H",
        "10H 30M",
        "11H",
        "11H 30M",
        "12H",
    ]
)
# Optional: define a minimum width of the combo box
combo_box.setMinimumContentsLength(15)
combo_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
combo_box.activated.connect(fechar_combo)

# Turn off button and labels
btn_desligar_agora = QToolButton()
btn_desligar_agora.setIcon(QIcon("public/images/power_off.png"))
btn_desligar_agora.setIconSize(QSize(64, 64))
btn_desligar_agora.setFixedSize(QSize(120, 120))
btn_desligar_agora.setStyleSheet("background-color: #E74C3C; border-radius: 10px;")

label_desligar = QLabel("Desligar Agora")
label_desligar.setAlignment(Qt.AlignmentFlag.AlignHCenter)
label_desligar.setStyleSheet("font-size: 10pt; font-weight: bold; color: white;")

# Schedule shutdown button and labels
btn_programar = QToolButton()
btn_programar.setIcon(QIcon("public/images/sleep_timer.png"))
btn_programar.setIconSize(QSize(64, 64))
btn_programar.setFixedSize(QSize(120, 120))
btn_programar.setStyleSheet("background-color: #2ECC71; border-radius: 10px;")

label_programar = QLabel("Programar")
label_programar.setAlignment(Qt.AlignmentFlag.AlignHCenter)
label_programar.setStyleSheet("font-size: 10pt; font-weight: bold; color: white;")

# Cancel shutdown button and labels
btn_cancel = QToolButton()
btn_cancel.setIcon(QIcon("public/images/cancel.png"))
btn_cancel.setIconSize(QSize(64, 64))
btn_cancel.setFixedSize(QSize(120, 120))
btn_cancel.setStyleSheet("background-color: #ff644b; border-radius: 10px;")

label_cancel = QLabel("Cancelar")
label_cancel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
label_cancel.setStyleSheet("font-size: 10pt; font-weight: bold; color: white;")

# Vertical layouts for each button + label
btn_desligar_layout = QVBoxLayout()
btn_desligar_layout.addWidget(btn_desligar_agora)
btn_desligar_layout.addWidget(label_desligar)

btn_programar_layout = QVBoxLayout()
btn_programar_layout.addWidget(btn_programar)
btn_programar_layout.addWidget(label_programar)

btn_cancel_layout = QVBoxLayout()
btn_cancel_layout.addWidget(btn_cancel)
btn_cancel_layout.addWidget(label_cancel)

# Horizontal layout for buttons
buttons_h_layout = QHBoxLayout()
buttons_h_layout.addStretch()
buttons_h_layout.addLayout(btn_desligar_layout)
buttons_h_layout.addSpacing(50)
buttons_h_layout.addLayout(btn_programar_layout)
buttons_h_layout.addSpacing(50)
buttons_h_layout.addLayout(btn_cancel_layout)
buttons_h_layout.addStretch()

# --- Connecting buttons to functions ---
btn_desligar_agora.clicked.connect(shutdown_confirmation)
btn_programar.clicked.connect(schedule_shutdown)
btn_cancel.clicked.connect(shutdown_cancel)


# --- Ordering the layout ---

# Horizontal Layout to "Sleep in" and ComboBox
top_h_layout = QHBoxLayout()
top_h_layout.addStretch()
top_h_layout.addWidget(label_sleep_in)
top_h_layout.addSpacing(10)
top_h_layout.addWidget(combo_box)
top_h_layout.addStretch()

# Layout Vertical Principal
main_v_layout = QVBoxLayout()
main_v_layout.addStretch(2)
main_v_layout.addLayout(top_h_layout)
main_v_layout.addStretch(1)
main_v_layout.addLayout(buttons_h_layout)
main_v_layout.addStretch(2)

# Define the main layout of the window
window.setLayout(main_v_layout)

# --- Window Styles ---
window.setStyleSheet(
    """
    QWidget {
        background-color: #333333;
        color: #FFFFFF;
    }
    QComboBox {
        background-color: #444444;
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 5px;
        color: #FFFFFF;
        selection-background-color: #0078D7;
    }
    QComboBox::drop-down {
        border: 0px;
    }
    QComboBox::down-arrow {
        image: url(public/images/dropdown.png);
        width: 15px;
        height: 15px;
        padding-right: 10px;
    }
    QPushButton {
        border: none;
        border-radius: 10px;
        padding: 10px;
    }
    QPushButton:hover {
        opacity: 0.8;
    }
    """
)

window.show()
sys.exit(app.exec())
