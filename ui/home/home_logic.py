from _colorize import Theme

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from core.theme_manager import ThemeManager


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add UI
        loadUi('ui/home/home.ui', self)

        # Add logo
        self.setWindowIcon(QIcon('ui/resources/logo/LOGO.png'))

        #Add themes
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.theme = ThemeManager()
        self.theme.apply_home_theme(self)

