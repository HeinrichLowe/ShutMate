from PyQt6.QtWidgets import (
    QWidget,
    QToolButton,
    QLabel,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from app.actions import schedule_shutdown, shutdown_cancel
from app.ui.shutdown_confirmation.shutdown_confirmation import ShutdownConfirmation
from app.utils.timer_options import TIMER_OPTIONS
from app.utils.css_loader import css_loader
from app.utils.resource_path import resource_path

# CSS Files
MAIN_CSS = css_loader(resource_path("app/assets/css/main_window.css"))

# App Icons
SHUTDOWN_ICON = resource_path("app/assets/images/shutmate.ico")
POWER_OFF_ICON = resource_path("app/assets/images/power_off.png")
SLEEP_TIMER_ICON = resource_path("app/assets/images/sleep_timer.png")
CANCEL_ICON = resource_path("app/assets/images/cancel.png")


class MainWindow(QWidget):
    """
    Main application window.

    This window provides the user interface for scheduling, confirming,
    and canceling system shutdowns.

    Args:
        parent (QWidget, optional): Parent widget. Defaults to None.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShutMate")
        self.setWindowIcon(QIcon(SHUTDOWN_ICON))
        self.setStyleSheet(MAIN_CSS)
        self.setMinimumSize(QSize(800, 600))

        # --- Widgets ---

        # Label "Sleep in:"
        self.label_sleep_in = QLabel("Sleep in:")
        self.label_sleep_in.setFont(QFont("Segoe UI", 12))

        # ComboBox (Dropdown)
        self.combo_box = QComboBox()
        self.combo_box.setMaxVisibleItems(10)
        self.combo_box.addItems(TIMER_OPTIONS)
        self.combo_box.setMinimumContentsLength(15)
        self.combo_box.setCursor(Qt.CursorShape.PointingHandCursor)
        self.combo_box.view().setCursor(Qt.CursorShape.PointingHandCursor)  # type: ignore
        self.combo_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        # Turn off button and labels
        self.btn_shutdown_now = QToolButton()
        self.btn_shutdown_now.setObjectName("shutdownNowButton")
        self.btn_shutdown_now.setIcon(QIcon(POWER_OFF_ICON))
        self.btn_shutdown_now.setIconSize(QSize(64, 64))
        self.btn_shutdown_now.setFixedSize(QSize(120, 120))
        self.btn_shutdown_now.setCursor(Qt.CursorShape.PointingHandCursor)

        self.label_shutdown = QLabel("Shutdown Now")
        self.label_shutdown.setObjectName("shutdownNowButtonLabel")
        self.label_shutdown.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Schedule shutdown button and labels
        self.btn_schedule = QToolButton()
        self.btn_schedule.setObjectName("scheduleButton")
        self.btn_schedule.setIcon(QIcon(SLEEP_TIMER_ICON))
        self.btn_schedule.setIconSize(QSize(64, 64))
        self.btn_schedule.setFixedSize(QSize(120, 120))
        self.btn_schedule.setCursor(Qt.CursorShape.PointingHandCursor)

        self.label_schedule = QLabel("Set Schedule")
        self.label_schedule.setObjectName("scheduleButtonLabel")
        self.label_schedule.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Cancel shutdown button and labels
        self.btn_cancel = QToolButton()
        self.btn_cancel.setObjectName("cancelButton")
        self.btn_cancel.setIcon(QIcon(CANCEL_ICON))
        self.btn_cancel.setIconSize(QSize(64, 64))
        self.btn_cancel.setFixedSize(QSize(120, 120))
        self.btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)

        self.label_cancel = QLabel("Cancel")
        self.label_cancel.setObjectName("cancelButtonLabel")
        self.label_cancel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Vertical layouts for each button + label
        self.btn_shutdown_layout = QVBoxLayout()
        self.btn_shutdown_layout.addWidget(self.btn_shutdown_now)
        self.btn_shutdown_layout.addWidget(self.label_shutdown)

        self.btn_schedule_layout = QVBoxLayout()
        self.btn_schedule_layout.addWidget(self.btn_schedule)
        self.btn_schedule_layout.addWidget(self.label_schedule)

        self.btn_cancel_layout = QVBoxLayout()
        self.btn_cancel_layout.addWidget(self.btn_cancel)
        self.btn_cancel_layout.addWidget(self.label_cancel)

        # Horizontal layout for buttons
        buttons_h_layout = QHBoxLayout()
        buttons_h_layout.addStretch()
        buttons_h_layout.addLayout(self.btn_shutdown_layout)
        buttons_h_layout.addSpacing(50)
        buttons_h_layout.addLayout(self.btn_schedule_layout)
        buttons_h_layout.addSpacing(50)
        buttons_h_layout.addLayout(self.btn_cancel_layout)
        buttons_h_layout.addStretch()

        # --- Connecting buttons to functions ---
        self.btn_shutdown_now.clicked.connect(lambda: ShutdownConfirmation(self).exec())
        self.btn_schedule.clicked.connect(
            lambda: schedule_shutdown(self, self.combo_box)
        )
        self.btn_cancel.clicked.connect(lambda: shutdown_cancel(self))

        # --- Ordering the layout ---

        # Horizontal Layout to "Sleep in" and ComboBox
        top_h_layout = QHBoxLayout()
        top_h_layout.addStretch()
        top_h_layout.addWidget(self.label_sleep_in)
        top_h_layout.addSpacing(10)
        top_h_layout.addWidget(self.combo_box)
        top_h_layout.addStretch()

        # Layout Vertical Principal
        main_v_layout = QVBoxLayout()
        main_v_layout.addStretch(2)
        main_v_layout.addLayout(top_h_layout)
        main_v_layout.addStretch(1)
        main_v_layout.addLayout(buttons_h_layout)
        main_v_layout.addStretch(2)

        # Define the main layout of the window
        self.setLayout(main_v_layout)
