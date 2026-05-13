class ThemeManager:
    def apply_login_theme(self, window):
        window.setStyleSheet("""
        QMainWindow{
            background-image: url(ui/resources/bg/login_bg.png);
            background-position: center;
            background-repeat: no-repeat;
        }
        
        QLabel#lbl_Username {
            color: white;
            font-weight: bold;
        }
        
        QLabel#lbl_Password {
            color: white;
            font-weight: bold;
        }
        
        QLabel#lbl_License {
            color: white;
        }
        
        QLabel#lbl_Version {
            color: white;
        }
        
        QLabel#lbl_Noti {
            color: white;
        }
        
        QPushButton#btn_SignIn {
            color: black;
            font-weight: bold;
        }
        """)

    def apply_loading_theme(self, window):
        window.setStyleSheet("""
        QMainWindow{
            background-image: url(ui/resources/bg/loading_bg.png);
            background-position: center;
            background-repeat: no-repeat;
        }
        
        QLabel#lbl_LoadingStatus {
            color: white;
            font-weight: bold;
        }
        
        QLabel#lbl_Loading {
            color: white;
            font-weight: bold;
        }
        
        QProgressBar#pb_LoadingPercent {
            color: white;
            font-weight: bold;
        }
        """)

    def apply_home_theme(self, window):
        window.setStyleSheet("""
        QMainWindow{
            background-color: #1e1f22;
        }
        QFrame#frame_TopBar{
            background-color: #222932;
        }
        """)
    

