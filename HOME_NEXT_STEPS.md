# Home Window Next Steps

## 1. Mục tiêu gần nhất

Home Window hiện đã có structure UI chính:

- `frame_TopBar`
- `frame_Body`
- `frame_Sidebar`
- `frame_MainVision`
- `frame_RightPanel`
- `frame_BottomLog`

Việc tiếp theo không nên mở rộng UI quá nhanh. Nên làm cho màn hình hiện tại bắt đầu có dữ liệu động, dễ kiểm tra và dễ bảo trì.

Thứ tự ưu tiên:

1. Thêm logic thời gian và event log.
2. Cấu hình bảng log và các bảng trong right panel.
3. Hoàn thiện style cho BottomLog và table.
4. Thêm navigation cho sidebar.
5. Thêm dữ liệu giả để kiểm tra trạng thái OK/NG.
6. Sau đó mới tích hợp camera/PLC/robot thật.

## 2. Bước 1: Thêm thời gian hệ thống

File cần sửa:

- `ui/home/home_logic.py`

Widget liên quan:

- `lbl_SystemTime`
- `lbl_CurrentLogTime`

Việc cần làm:

- Tạo `QTimer` chạy mỗi 1 giây.
- Cập nhật thời gian hiện tại lên TopBar.
- Cập nhật thời gian hiện tại ở BottomLog.

Định dạng gợi ý:

```text
2026-05-14 14:30:25
```

Object cần dùng:

```text
QTimer
QDateTime
```

## 3. Bước 2: Setup Event Log

Widget liên quan:

- `tbl_EventLog`

Cấu trúc cột gợi ý:

```text
Time | Level | Source | Message
```

Vì BottomLog chỉ cao khoảng 48px, nên bảng log cần gọn:

- Ẩn vertical header.
- Không cho edit cell.
- Chọn cả row khi click.
- Tắt hoặc giảm chiều cao horizontal header nếu quá chật.
- Chỉ giữ 1-2 dòng log mới nhất.

API logic nên có:

```python
add_event_log(level: str, source: str, message: str)
```

Level gợi ý:

```text
INFO
WARNING
ERROR
```

Dòng log mẫu khi mở Home:

```text
INFO | System | Home window loaded
INFO | System | Waiting for machine status
```

## 4. Bước 3: Setup Right Panel Tables

Widget liên quan:

- `tbl_Measurements`
- `tbl_DeviceStatus`

`tbl_Measurements` nên có cột:

```text
Item | Value | Min | Max | Status
```

`tbl_DeviceStatus` nên có cột:

```text
Device | Status
```

Dữ liệu giả ban đầu:

```text
Camera | Offline
PLC | Offline
Robot | Offline
Database | Ready
```

Mục tiêu của bước này:

- Kiểm tra table style.
- Kiểm tra layout right panel.
- Chuẩn bị cho dữ liệu thật sau này.

## 5. Bước 4: Thêm trạng thái giả cho inspection

Widget liên quan:

- `lbl_FinalResult`
- `lbl_ResultReason`
- `lbl_LastCycleTime`
- `lbl_TotalCounter`
- `lbl_OKCounter`
- `lbl_NGCounter`
- `lbl_YieldPercent`
- `lbl_ImageStatus`

Việc cần làm:

- Tạo hàm cập nhật trạng thái inspection.
- Ban đầu dùng dữ liệu giả.
- Có thể thêm nút `btn_SaveImage` hoặc `btn_FitView` để trigger fake result tạm thời nếu cần test UI.

State gợi ý:

```text
WAIT
OK
NG
ERROR
```

Màu nên được điều khiển bằng dynamic property hoặc stylesheet class sau này. Trước mắt có thể chỉ đổi text.

## 6. Bước 5: Hoàn thiện Sidebar Navigation

Widget liên quan:

- `btn_RunPage`
- `btn_ApplicationPage`
- `btn_CameraPage`
- `btn_IOPage`
- `btn_AlarmPage`
- `btn_HistoryPage`
- `btn_SettingsPage`

Hiện tại sidebar mới có button. Bước tiếp theo là quyết định cách chuyển page.

Khuyến nghị:

- Dùng `QStackedWidget` trong `frame_MainVision` hoặc trong `frame_Body`.
- Mỗi button đổi sang một page.
- Bắt đầu với 2 page trước:
  - Run
  - Application

Không nên làm đủ 7 page ngay từ đầu. Nên dựng navigation cơ bản trước, rồi mở rộng.

## 7. Bước 6: Chuẩn hóa theme và UI behavior

File cần sửa:

- `core/theme_manager.py`

Việc cần làm:

- Style riêng cho `tbl_EventLog`.
- Style trạng thái button active trong sidebar.
- Style OK/NG/ERROR cho `lbl_FinalResult`.
- Kiểm tra text có bị tràn ở sidebar width hiện tại không.

Ghi chú:

- Nếu sidebar giữ width `100px`, text như `Applications` có thể hơi chật.
- Nếu dùng icon + text, nên tăng sidebar lên `180-200px`.
- Nếu dùng icon-only, giữ `80-100px` là hợp lý.

## 8. Bước 7: Tách logic Home thành helper nhỏ

Khi `home_logic.py` bắt đầu dài, nên tách các nhóm logic:

```text
setup_time()
setup_event_log()
setup_tables()
setup_sidebar()
add_event_log()
update_machine_status()
update_inspection_result()
```

Mục tiêu:

- `__init__()` dễ đọc.
- Mỗi phần logic có trách nhiệm rõ.
- Sau này tích hợp camera/PLC không làm file bị rối.

## 9. Bước 8: Tích hợp thiết bị thật sau cùng

Chỉ nên tích hợp thiết bị thật sau khi UI và dữ liệu giả ổn.

Thứ tự tích hợp nên là:

1. Camera.
2. PLC.
3. Robot.
4. Database/log storage.

Mỗi thiết bị nên có service riêng trong `services/` hoặc module riêng trong `core/`.

Ví dụ:

```text
services/camera_service.py
services/plc_service.py
services/robot_service.py
services/log_service.py
```

## 10. Checklist thực hiện ngắn hạn

- [ ] Update `home_logic.py` để chạy timer thời gian.
- [ ] Setup `tbl_EventLog`.
- [ ] Thêm hàm `add_event_log()`.
- [ ] Thêm log mẫu khi vào Home.
- [ ] Setup `tbl_Measurements`.
- [ ] Setup `tbl_DeviceStatus`.
- [ ] Cập nhật text mặc định cho result/counter/status.
- [ ] Kiểm tra lại giao diện bằng cách chạy `main.py`.
- [ ] Sau khi ổn, bắt đầu thiết kế sidebar navigation.

## 11. Ưu tiên hiện tại

Việc nên làm ngay tiếp theo:

```text
Implement time + event log in ui/home/home_logic.py
```

Đây là bước nhỏ nhưng làm Home Window bắt đầu có hành vi động, giúp kiểm tra layout và theme thực tế trước khi phát triển các tính năng lớn hơn.

