from PyQt6.QtCore import Qt, QThread
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from core.sys_initializer import SysInit
from core.theme_manager import ThemeManager


class LoadingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add UI
        loadUi('ui/loading/loading.ui', self)

        # Add logo
        self.setWindowIcon(QIcon('ui/resources/logo/LOGO.png'))

        # Add themes
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # Add callbacks
        self.on_loading_finished = None

        #
        self.theme = ThemeManager()

        self.theme.apply_loading_theme(self)

        # No cover and always on-top (if necessary)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.thread = QThread()

        self.worker = SysInit()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.progress.connect(self.update_progress)

        self.worker.finished.connect(self.thread.quit)

        self.worker.finished.connect(self.on_finished)

        self.thread.start()

    def update_progress(self, progress, step):
        self.pb_LoadingPercent.setValue(progress)
        self.lbl_LoadingStatus.setText(step)

    def on_finished(self):
        if self.on_loading_finished:
            self.on_loading_finished()