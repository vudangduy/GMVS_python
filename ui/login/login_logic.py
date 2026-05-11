from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from core.theme_manager import ThemeManager
from services.auth_service import AuthService


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add ui
        loadUi('ui/login/login.ui', self)

        # Add logo
        self.setWindowIcon(QIcon('ui/resources/logo/LOGO.png'))

        # Fixed size
        self.setFixedSize(500,400)

        # Add themes
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.theme = ThemeManager()
        self.theme.apply_login_theme(self)
        # Add service (later)
        self.auth_service = AuthService()

        # Load and config signal
        self.li_Username.setFocus()
        self.li_Password.returnPressed.connect(self.handle_login)
        self.btn_SignIn.clicked.connect(self.handle_login)

        # Add callback components
        self.on_login_success = None

    def handle_login(self):

        username = self.li_Username.text()
        password = self.li_Password.text()

        if self.auth_service.login(username, password):
            self.lbl_Noti.setText('Login successful, please wait...')
            if self.on_login_success:
                self.on_login_success()
        else:
            self.lbl_Noti.setText('Login failed, please try again...')

