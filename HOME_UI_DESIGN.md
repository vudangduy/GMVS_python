# Gợi ý thiết kế giao diện Home

## 1. Mục tiêu màn hình Home

Màn hình Home nên là màn hình vận hành chính cho ứng dụng vision machine trong môi trường industrial. Ưu tiên thiết kế:

- Nhận biết trạng thái máy nhanh trong 1-2 giây.
- Camera/live image nằm ở trung tâm và chiếm diện tích lớn nhất.
- Kết quả inspection OK/NG rõ ràng, màu sắc mạnh nhưng không gây rối mắt.
- Các nút vận hành quan trọng dễ bấm, có kích thước lớn, khoảng cách tốt.
- Thông tin kỹ thuật được sắp xếp thành panel để operator hoặc lập trình viên dễ đọc.
- Layout ổn định cho màn hình PC 1920x1080, phù hợp khi chạy maximized.

## 2. Hướng thiết kế tổng thể

Style nên là industrial dashboard, không phải landing page. Giao diện nên đậm, gọn, tập trung vào dữ liệu và trạng thái.

Đề xuất bố cục:

```text
+--------------------------------------------------------------------------------+
| Top Bar: Logo | Machine Name | Application | PLC/Robot/Camera/DB | User | Time  |
+------------+---------------------------------------------------+---------------+
| Left Menu  | Main Vision Area                                  | Right Panel   |
|            |                                                   |               |
| Run        | +-----------------------------------------------+ | Result        |
| Application| | Live Camera / Last Image                      | | OK/NG         |
| Camera     | | ROI Overlay / Defect Boxes / Crosshair        | | Score         |
| IO         | | Zoom / Fit / Save Image                       | | Measurements  |
| Alarm      | +-----------------------------------------------+ | Device Status |
| Settings   |                                                   | Statistics    |
+------------+---------------------------------------------------+---------------+
| Bottom Bar: Current time | Event log                                      |
+--------------------------------------------------------------------------------+
```

## 3. Structure Tree đề xuất

Structure tree dưới đây mô tả cách sắp xếp widget theo quan hệ cha-con. Có thể dùng làm hướng dẫn khi dựng `home.ui` bằng Qt Designer.

```text
wd_Home (QMainWindow)
+-- centralwidget (QWidget)
    +-- layout_Root (QVBoxLayout)
        +-- frame_TopBar (QFrame)
        |   +-- layout_TopBar (QHBoxLayout)
        |       +-- lbl_Logo (QLabel)
        |       +-- lbl_MachineName (QLabel)
        |       +-- lbl_CurrentApplication (QLabel)
        |       +-- spacer_TopBarLeft (QSpacerItem)
        |       +-- lbl_CameraStatus (QLabel)
        |       +-- lbl_PLCStatus (QLabel)
        |       +-- lbl_RobotStatus (QLabel)
        |       +-- lbl_DBStatus (QLabel)
        |       +-- lbl_CurrentUser (QLabel)
        |       +-- lbl_SystemTime (QLabel)
        |
        +-- frame_Body (QFrame)
        |   +-- layout_Body (QHBoxLayout)
        |       +-- frame_Sidebar (QFrame)
        |       |   +-- layout_Sidebar (QVBoxLayout)
        |       |       +-- btn_RunPage (QPushButton)
        |       |       +-- btn_ApplicationPage (QPushButton)
        |       |       +-- btn_CameraPage (QPushButton)
        |       |       +-- btn_IOPage (QPushButton)
        |       |       +-- btn_AlarmPage (QPushButton)
        |       |       +-- btn_HistoryPage (QPushButton)
        |       |       +-- spacer_Sidebar (QSpacerItem)
        |       |       +-- btn_SettingsPage (QPushButton)
        |       |
        |       +-- frame_MainVision (QFrame)
        |       |   +-- layout_MainVision (QVBoxLayout)
        |       |       +-- frame_CameraToolbar (QFrame)
        |       |       |   +-- layout_CameraToolbar (QHBoxLayout)
        |       |       |       +-- lbl_ImageStatus (QLabel)
        |       |       |       +-- spacer_CameraToolbar (QSpacerItem)
        |       |       |       +-- btn_ZoomIn (QPushButton)
        |       |       |       +-- btn_ZoomOut (QPushButton)
        |       |       |       +-- btn_FitView (QPushButton)
        |       |       |       +-- btn_SaveImage (QPushButton)
        |       |       |
        |       |       +-- frame_CameraView (QFrame)
        |       |           +-- layout_CameraView (QVBoxLayout)
        |       |               +-- lbl_CameraImage (QLabel)
        |       |               +-- frame_OverlayInfo (QFrame)
        |       |
        |       +-- frame_RightPanel (QFrame)
        |           +-- layout_RightPanel (QVBoxLayout)
        |               +-- frame_ResultSummary (QFrame)
        |               |   +-- layout_ResultSummary (QVBoxLayout)
        |               |       +-- lbl_FinalResult (QLabel)
        |               |       +-- lbl_ResultReason (QLabel)
        |               |       +-- lbl_LastCycleTime (QLabel)
        |               |
        |               +-- frame_Measurements (QFrame)
        |               |   +-- layout_Measurements (QVBoxLayout)
        |               |       +-- lbl_MeasurementsTitle (QLabel)
        |               |       +-- tbl_Measurements (QTableWidget)
        |               |
        |               +-- frame_DeviceStatus (QFrame)
        |               |   +-- layout_DeviceStatus (QVBoxLayout)
        |               |       +-- lbl_DeviceStatusTitle (QLabel)
        |               |       +-- tbl_DeviceStatus (QTableWidget)
        |               |
        |               +-- frame_Statistics (QFrame)
        |                   +-- layout_Statistics (QGridLayout)
        |                       +-- lbl_TotalCounter (QLabel)
        |                       +-- lbl_OKCounter (QLabel)
        |                       +-- lbl_NGCounter (QLabel)
        |                       +-- lbl_YieldPercent (QLabel)
        |
        +-- frame_BottomLog (QFrame)
            +-- layout_BottomLog (QHBoxLayout)
                +-- lbl_CurrentLogTime (QLabel)
                +-- tbl_EventLog (QTableWidget)

```

Ghi chú khi dựng structure:

- `frame_TopBar`, `frame_Body`, `frame_BottomLog` là 3 vùng chính theo chiều dọc.
- `frame_Body` chứa 3 vùng ngang: sidebar, camera view, result panel.
- `frame_MainVision` chỉ nên tập trung vào ảnh, overlay và toolbar camera.
- `frame_RightPanel` chứa các thông tin kết quả và thiết bị, không nên đặt log dài ở đây.
- `frame_BottomLog` chỉ chứa thời gian hiện tại và event log để theo dõi lịch sử vận hành gần nhất.
- Nếu chưa cần nhiều page, có thể bỏ `frame_Sidebar` ở version đầu và thêm sau.

## 4. Vùng Top Bar

Top bar hiện tại đang có chiều cao 50px. Có thể giữ 50-60px, nhưng nên đổi object name từ `frame` thành `frame_TopBar` để khớp với `ThemeManager.apply_home_theme()`.

Thành phần nên có:

- Logo bên trái: `lbl_Logo`, kích thước 50x50.
- Tên ứng dụng/máy: `lbl_MachineName`, ví dụ `GMVS - Vision Inspection`.
- Application đang chạy: `lbl_CurrentApplication`.
- Trạng thái kết nối:
  - `lbl_CameraStatus`: Camera Online/Offline.
  - `lbl_PLCStatus`: PLC Online/Offline.
  - `lbl_RobotStatus`: Robot Online/Offline.
  - `lbl_DBStatus`: Database Online/Offline.
- User hiện tại: `lbl_CurrentUser`.
- Thời gian hệ thống: `lbl_SystemTime`.

Màu gợi ý:

- Nền top bar: `#222932`
- Text chính: `#F5F7FA`
- Text phụ: `#A7B0BC`
- Online: `#20C997`
- Warning: `#FFC857`
- Offline/NG: `#FF4D4F`

## 5. Left Navigation

Bên trái nên là menu dọc có chiều rộng 72-96px nếu chỉ dùng icon, hoặc 180-220px nếu dùng icon + text. Với ứng dụng industrial, icon + text thường dễ đọc hơn cho operator.

Menu đề xuất:

- Run
- Application
- Camera
- IO
- Alarm
- History
- Settings

Object name gợi ý:

- `frame_Sidebar`
- `btn_RunPage`
- `btn_ApplicationPage`
- `btn_CameraPage`
- `btn_IOPage`
- `btn_AlarmPage`
- `btn_HistoryPage`
- `btn_SettingsPage`

Trạng thái active nên có viền trái hoặc nền khác màu. Không nên dùng quá nhiều màu trong menu; chỉ cần nền đậm và active accent.

## 6. Main Vision Area

Đây là vùng quan trọng nhất, nên chiếm khoảng 60-70% chiều rộng màn hình.

Thành phần nên có:

- `frame_CameraView`: khung hiển thị ảnh live hoặc ảnh inspection mới nhất.
- `lbl_CameraImage`: label dùng để render frame/image.
- `frame_OverlayInfo`: lớp thông tin phụ như FPS, exposure, gain, trigger mode.
- `btn_ZoomIn`, `btn_ZoomOut`, `btn_FitView`, `btn_SaveImage`.
- `lbl_ImageStatus`: hiển thị `LIVE`, `LAST NG`, `NO IMAGE`, hoặc `TRIGGER WAIT`.

Nội dung visual nên ưu tiên:

- Ảnh camera nên có nền đen/xám đậm khi chưa có ảnh.
- ROI nên hiển thị bằng viền màu cyan hoặc yellow.
- Defect box:
  - OK/Pass: xanh lá.
  - NG/Fail: đỏ.
  - Warning: vàng.
- Crosshair/center line nên mỏng, không che ảnh.

## 7. Right Result Panel

Panel bên phải nên hiển thị kết quả mới nhất và thông số đo. Chiều rộng gợi ý 320-420px.

Thành phần nên có:

- `frame_ResultSummary`
  - `lbl_FinalResult`: OK/NG lớn, rõ.
  - `lbl_ResultReason`: lý do NG hoặc summary.
  - `lbl_LastCycleTime`: cycle time.
- `frame_Measurements`
  - Bảng kết quả đo: item, value, min, max, status.
  - Widget gợi ý: `QTableWidget` hoặc `QTreeWidget`.
- `frame_DeviceStatus`
  - Camera
  - Light controller
  - PLC
  - Trigger sensor
  - Database
- `frame_Statistics`
  - Total
  - OK count
  - NG count
  - Yield %

Màu kết quả:

- OK: nền xanh `#123D2F`, text `#20C997`
- NG: nền đỏ đậm `#4A1D24`, text `#FF4D4F`
- Idle: nền xám `#2A3038`, text `#C9D1D9`

Không nên chỉ dựa vào màu. Nên có text `OK`, `NG`, `WAIT`, `ERROR` thật rõ.

## 8. Bottom Bar và Event Log

Vùng dưới nên cao 120-180px nếu cần log liên tục, hoặc 40-60px nếu chỉ cần summary.

Gợi ý chia thành:

- `lbl_CurrentLogTime`: thời gian hiện tại.
- `tbl_EventLog`: bảng log thời gian, level, source, message.

Level log:

- INFO: xanh/cyan nhẹ.
- WARNING: vàng.
- ERROR/ALARM: đỏ.

## 9. Bố cục kích thước gợi ý cho 1920x1080

Nếu chạy maximized 1920x1080:

```text
Top bar:        x=0,   y=0,    w=1920, h=56
Sidebar:        x=0,   y=56,   w=200,  h=884
Main vision:    x=200, y=56,   w=1280, h=884
Right panel:    x=1480,y=56,   w=440,  h=884
Bottom bar/log: x=0,   y=940,  w=1920, h=140
```

Nếu muốn giản hơn:

```text
Top bar:        56px
Sidebar:        180px
Right panel:    380px
Bottom log:     120px
Main vision:    phần còn lại
```

Nên dùng layout thay vì geometry cố định nếu có thể:

- `QVBoxLayout` cho màn hình chính.
- `QHBoxLayout` cho khu vực body.
- `QFrame` để chia từng panel.
- `QSplitter` nếu muốn user kéo thay đổi kích thước camera/log.

## 10. Object Name đề xuất

Đặt objectName rõ ràng sẽ giúp stylesheet và logic dễ bảo trì.

```text
centralwidget
frame_TopBar
lbl_Logo
lbl_MachineName
lbl_CurrentApplication
lbl_CameraStatus
lbl_PLCStatus
lbl_RobotStatus
lbl_DBStatus
lbl_CurrentUser
lbl_SystemTime

frame_Sidebar
btn_RunPage
btn_ApplicationPage
btn_CameraPage
btn_IOPage
btn_AlarmPage
btn_HistoryPage
btn_SettingsPage

frame_MainVision
frame_CameraToolbar
btn_ZoomIn
btn_ZoomOut
btn_FitView
btn_SaveImage
lbl_ImageStatus
frame_CameraView
lbl_CameraImage

frame_RightPanel
frame_ResultSummary
lbl_FinalResult
lbl_ResultReason
lbl_LastCycleTime
tbl_Measurements
frame_DeviceStatus
frame_Statistics

frame_BottomLog
lbl_CurrentLogTime
tbl_EventLog
```

## 11. Màu sắc và typography

Palette gợi ý:

```text
App background:      #1E1F22
Panel background:    #252A31
Panel border:        #343B45
Top bar:             #222932
Sidebar:             #20252B
Primary text:        #F5F7FA
Secondary text:      #A7B0BC
Muted text:          #6F7A86
Accent cyan:         #31C6D4
OK green:            #20C997
NG red:              #FF4D4F
Warning yellow:      #FFC857
```

Font:

- Label thông tin: 12-14px.
- Heading panel: 14-16px bold.
- Kết quả OK/NG: 48-72px bold.
- Counter/statistic: 20-28px bold.

## 12. Trạng thái cần thiết

Màn hình Home nên có đủ các state sau:

- Idle: chưa trigger, đang chờ sản phẩm.
- Running: camera/PLC đang online, sẵn sàng inspection.
- Inspecting: đang xử lý ảnh.
- OK: sản phẩm đạt.
- NG: sản phẩm lỗi, hiển thị lý do.
- Alarm: có lỗi hệ thống, cần operator can thiệp.
- Offline: camera/PLC/database mất kết nối.

Mỗi state nên có:

- Text rõ ràng.
- Màu tương ứng.
- Log tương ứng.
- Nếu là lỗi, hiển thị nguồn lỗi và hành động gợi ý ngắn gọn.

## 13. Ưu tiên thiết kế cho operator

Operator trong nhà máy cần thông tin nhanh hơn là giao diện đẹp. Nên ưu tiên:

- Nút Start/Stop/Reset lớn và dễ thấy.
- Kết quả OK/NG rất lớn, không cần đọc bảng mới biết.
- Alarm mới nhất luôn hiển thị trên màn hình.
- Counter OK/NG/Total luôn thấy được.
- Hình ảnh lỗi gần nhất có thể xem lại nhanh.
- Không đặt các nút nguy hiểm gần nút vận hành thường xuyên.

Nút quan trọng gợi ý:

- `btn_StartRun`
- `btn_StopRun`
- `btn_ResetAlarm`
- `btn_ManualTrigger`
- `btn_SaveNGImage`

Nút nguy hiểm như Stop/Reset nên có màu riêng và cần confirm nếu tác động lớn.

## 14. Phiên bản Home UI để bắt đầu

Nếu cần làm nhanh version đầu tiên, nên build theo thứ tự:

1. Top bar có logo, tên máy, application, status camera/PLC/robot/user/time.
2. Main camera view chiếm trung tâm.
3. Right panel có OK/NG, cycle time, measurements, counters.
4. Bottom log hiển thị thời gian hiện tại và event log.
5. Sidebar thêm sau nếu đã có nhiều page.

Đây là version phù hợp với project hiện tại vì `home.ui` mới có top bar và logo. Có thể mở rộng dần mà không cần thay đổi flow `WindowManager`.
