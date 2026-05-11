class AuthService:
    def __init__(self):
        # Fake database
        self.user_info = {
            "admin" : "1",
            "operator" : "2"
        }

    def login(self, username: str, password: str) -> bool:

        if not username or not password:
            return False

        if username not in self.user_info:
            return False

        if self.user_info[username] != password:
            return False

        return True