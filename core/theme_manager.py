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
        QMainWindow {
            background-color: #1E1F22;
        }

        QWidget#centralwidget {
            background-color: #1E1F22;
        }

        QFrame {
            border: none;
        }

        QLabel {
            color: #F5F7FA;
            font-size: 13px;
        }

        QPushButton {
            background-color: #2A3038;
            color: #F5F7FA;
            border: 1px solid #343B45;
            padding: 8px 10px;
            font-size: 12px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #343B45;
            border: 1px solid #31C6D4;
        }

        QPushButton:pressed {
            background-color: #31C6D4;
            color: #101418;
        }

        QFrame#frame_TopBar {
            background-color: #222932;
            border-bottom: 1px solid #343B45;
        }
        
        QLabel#lbl_Logo {
            color: #F5F7FA;
            font-weight: bold;
        }

        QLabel#lbl_MachineName {
            color: #F5F7FA;
            font-size: 16px;
            font-weight: bold;
        }

        QLabel#lbl_CurrentApplication,
        QLabel#lbl_CurrentUser,
        QLabel#lbl_SystemTime {
            color: #A7B0BC;
            font-size: 13px;
        }

        QLabel#lbl_CameraStatus,
        QLabel#lbl_PLCStatus,
        QLabel#lbl_RobotStatus,
        QLabel#lbl_DBStatus {
            color: #20C997;
            font-size: 13px;
            font-weight: bold;
        }

        QFrame#frame_Body {
            background-color: #1E1F22;
            border: none;
        }

        QFrame#frame_Sidebar {
            background-color: #20252B;
            border-right: 1px solid #343B45;
        }

        QFrame#frame_Sidebar QPushButton {
            background-color: transparent;
            color: #A7B0BC;
            border: none;
            padding: 10px 6px;
            text-align: left;
        }

        QFrame#frame_Sidebar QPushButton:hover {
            background-color: #2E3640;
            color: #F5F7FA;
        }

        QFrame#frame_Sidebar QPushButton:pressed {
            background-color: #31C6D4;
            color: #101418;
        }

        QFrame#frame_MainVision {
            background-color: #1E1F22;
            border: none;
        }

        QFrame#frame_CameraToolbar {
            background-color: #252A31;
            border-bottom: 1px solid #343B45;
        }

        QFrame#frame_CameraView {
            background-color: #101418;
            border: 1px solid #343B45;
        }

        QLabel#lbl_ImageStatus {
            color: #31C6D4;
            font-weight: bold;
        }

        QLabel#lbl_CameraImage {
            color: #6F7A86;
            font-size: 18px;
            font-weight: bold;
        }

        QFrame#frame_OverlayInfo {
            background-color: #151A20;
            border-top: 1px solid #343B45;
        }

        QFrame#frame_RightPanel {
            background-color: #252A31;
            border-left: 1px solid #343B45;
        }

        QFrame#frame_ResultSummary,
        QFrame#frame_Measurements,
        QFrame#frame_DeviceStatus,
        QFrame#frame_Statistics {
            background-color: #252A31;
            border-bottom: 1px solid #343B45;
        }

        QLabel#lbl_FinalResult {
            color: #20C997;
            font-size: 42px;
            font-weight: bold;
        }

        QLabel#lbl_ResultReason,
        QLabel#lbl_LastCycleTime,
        QLabel#lbl_MeasurementsTitle,
        QLabel#lbl_DeviceStatusTitle {
            color: #A7B0BC;
            font-size: 13px;
            font-weight: bold;
        }

        QLabel#lbl_TotalCounter,
        QLabel#lbl_OKCounter,
        QLabel#lbl_NGCounter,
        QLabel#lbl_YieldPercent {
            color: #F5F7FA;
            font-size: 13px;
            font-weight: bold;
        }

        QTableWidget {
            background-color: #1E1F22;
            color: #F5F7FA;
            gridline-color: #343B45;
            border: 1px solid #343B45;
            selection-background-color: #31C6D4;
            selection-color: #101418;
        }

        QHeaderView::section {
            background-color: #20252B;
            color: #A7B0BC;
            border: 1px solid #343B45;
            padding: 4px;
            font-weight: bold;
        }

        QFrame#frame_BottomLog {
            background-color: #252A31;
            border-top: 1px solid #343B45;
        }

        QLabel#lbl_CurrentLogTime {
            background-color: #1E1F22;
            color: #A7B0BC;
            border: 1px solid #343B45;
            padding: 4px 8px;
            font-size: 12px;
            font-weight: bold;
        }

        QTableWidget#tbl_EventLog {
            background-color: #1E1F22;
            color: #F5F7FA;
            gridline-color: #343B45;
            border: 1px solid #343B45;
            selection-background-color: #31C6D4;
            selection-color: #101418;
            font-size: 12px;
        }

        QTableWidget#tbl_EventLog::item {
            padding: 2px 4px;
        }

        QTableWidget#tbl_EventLog QHeaderView::section {
            background-color: #20252B;
            color: #A7B0BC;
            border: none;
            padding: 2px 4px;
            font-size: 11px;
            font-weight: bold;
        }
        """)
    
