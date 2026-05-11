from ui.home.home_logic import HomeWindow
from ui.login.login_logic import LoginWindow
from ui.loading.loading_logic import LoadingWindow

class WindowManager():
    def __init__(self):
        self.login_window = None
        self.loading_window = None
        self.home_window = None

    def start(self):
        self.show_login()

    def show_login(self):
        self.login_window = LoginWindow()
        self.login_window.on_login_success = self.show_loading
        self.login_window.show()

    def show_loading(self):
        self.loading_window = LoadingWindow()
        self.loading_window.on_loading_finished = self.show_home
        self.login_window.close()
        self.loading_window.show()

    def show_home(self):
        self.home_window = HomeWindow()
        self.loading_window.close()
        self.home_window.show()
