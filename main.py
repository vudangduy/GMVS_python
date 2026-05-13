import sys

from PyQt6.QtWidgets import QApplication

from core.window_manager import WindowManager

app = QApplication(sys.argv)

window_manager = WindowManager()

window_manager.start()

sys.exit(app.exec())