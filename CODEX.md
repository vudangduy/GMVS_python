# GMVS Python Project

## 1. Tong quan

Day la project ung dung desktop viet bang Python va PyQt6. Ung dung hien tai co 3 man hinh chinh:

- Login: nguoi dung nhap username/password de dang nhap.
- Loading: hien tien trinh khoi tao he thong sau khi dang nhap thanh cong.
- Home: man hinh chinh cua ung dung sau khi loading hoan tat.

Kien truc project dang di theo huong tach ro:

- `main.py`: diem khoi chay ung dung.
- `core/`: cac thanh phan dieu phoi va logic he thong dung chung.
- `services/`: cac service nghiep vu, hien tai co xac thuc dang nhap.
- `ui/`: file giao dien `.ui`, logic cua tung man hinh va tai nguyen hinh anh.

## 2. Cau truc thu muc

```text
GMVS_python/
+-- main.py
+-- core/
|   +-- window_manager.py
|   +-- theme_manager.py
|   +-- sys_initializer.py
+-- services/
|   +-- auth_service.py
+-- ui/
    +-- login/
    |   +-- login.ui
    |   +-- login_logic.py
    +-- loading/
    |   +-- loading.ui
    |   +-- loading_logic.py
    +-- home/
    |   +-- home.ui
    |   +-- home_logic.py
    +-- resources/
        +-- bg/
        +-- icons/
        +-- logo/
```

## 3. Diem khoi chay

File `main.py` tao `QApplication`, khoi tao `WindowManager`, goi `window_manager.start()` va bat dau Qt event loop bang `app.exec()`.

Luong chay:

```text
main.py
+-- WindowManager.start()
    +-- show_login()
```

## 4. Dieu huong man hinh

`core/window_manager.py` la noi quan ly vong doi cua cac cua so:

```text
LoginWindow
    +-- dang nhap thanh cong
        +-- LoadingWindow
            +-- loading hoan tat
                +-- HomeWindow
```

Chi tiet:

- `show_login()`: tao va hien `LoginWindow`.
- `show_loading()`: tao `LoadingWindow`, dong login window, hien loading window.
- `show_home()`: tao `HomeWindow`, dong loading window, hien home window.

Co che chuyen man hinh hien tai dung callback:

- `LoginWindow.on_login_success`
- `LoadingWindow.on_loading_finished`

## 5. Man hinh Login

File lien quan:

- `ui/login/login.ui`
- `ui/login/login_logic.py`
- `services/auth_service.py`

`LoginWindow` load giao dien tu `ui/login/login.ui`, ap dung theme login va ket noi su kien:

- `li_Password.returnPressed` goi `handle_login`.
- `btn_SignIn.clicked` goi `handle_login`.

Thong tin dang nhap hien tai duoc kiem tra trong `AuthService`.

Tai khoan mau:

```text
admin / 1
operator / 2
```

Neu dang nhap thanh cong:

- `lbl_Noti` hien thong bao thanh cong.
- callback `on_login_success` duoc goi de chuyen sang loading.

Neu that bai:

- `lbl_Noti` hien thong bao dang nhap that bai.

## 6. Man hinh Loading

File lien quan:

- `ui/loading/loading.ui`
- `ui/loading/loading_logic.py`
- `core/sys_initializer.py`

`LoadingWindow` load giao dien tu `ui/loading/loading.ui`, ap dung theme loading va chay tien trinh khoi tao qua `QThread`.

`SysInit` la worker ke thua `QObject`, co 2 signal:

- `progress(int, str)`: cap nhat phan tram va noi dung buoc dang chay.
- `finished()`: bao hieu qua trinh khoi tao da xong.

Qua trinh khoi tao hien tai gom 10 buoc gia lap, moi buoc tam dung 1 giay bang `time.sleep(1)`.

Khi co progress:

- `pb_LoadingPercent` duoc cap nhat gia tri.
- `lbl_LoadingStatus` duoc cap nhat noi dung.

Khi hoan tat:

- thread dung lai.
- callback `on_loading_finished` duoc goi de chuyen sang Home.

## 7. Man hinh Home

File lien quan:

- `ui/home/home.ui`
- `ui/home/home_logic.py`

`HomeWindow` load giao dien tu `ui/home/home.ui`, ap dung theme home va hien cua so o che do maximized bang `showMaximized()`.

Giao dien Home hien tai con don gian, gom main window, central widget, mot frame va status bar. Day co ve la noi se phat trien cac chuc nang chinh cua GMVS.

## 8. Quan ly theme va tai nguyen

`core/theme_manager.py` tap trung stylesheet cho tung man hinh:

- `apply_login_theme(window)`
- `apply_loading_theme(window)`
- `apply_home_theme(window)`

Tai nguyen hinh anh nam trong:

- `ui/resources/bg/`: background cho login/loading.
- `ui/resources/logo/`: logo ung dung.
- `ui/resources/icons/`: icon nhieu kich thuoc.

Theme hien tai dung duong dan tuong doi den cac file anh, vi vay nen chay ung dung tu root project `GMVS_python/`.

## 9. Phu thuoc

Project dang dung:

- Python
- PyQt6

Chua thay file quan ly dependency nhu `requirements.txt` hay `pyproject.toml`. Neu can cai moi moi truong, nen tao file dependency rieng, toi thieu gom:

```text
PyQt6
```

## 10. Cach chay ung dung

Tu thu muc root project:

```powershell
python main.py
```

Neu dung virtual environment co san:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

## 11. Ghi chu ky thuat

- Cac file `.ui` duoc load runtime bang `PyQt6.uic.loadUi`, nen thay doi UI co the duoc thuc hien bang Qt Designer.
- `AuthService` hien la fake database trong memory, phu hop cho prototype.
- `SysInit` hien la logic gia lap loading, chua thuc hien khoi tao that su.
- `WindowManager` giu reference den cac window de tranh bi garbage collected.
- Ung dung phu thuoc vao duong dan tuong doi, nen viec chay tu sai working directory co the lam loi load `.ui` hoac asset.

## 12. Huong phat trien de xuat

- Them `requirements.txt` de co the cai dat moi truong lap lai duoc.
- Chuyen fake user trong `AuthService` sang database, file config hoac API tuy theo muc tieu san pham.
- Tach cac duong dan asset/UI thanh constant hoac helper de de bao tri.
- Them xu ly loi khi load UI, load icon/background hoac khi khoi tao he thong that bai.
- Don dep import khong dung trong mot so file logic.
- Them test don vi cho `AuthService` va cac logic nghiep vu khong phu thuoc UI.

## 13. Tom tat kien truc

Project hien tai la mot prototype PyQt6 co cau truc ro rang:

```text
Entry point: main.py
Window flow: WindowManager
UI screens: Login -> Loading -> Home
Business service: AuthService
System startup simulation: SysInit
Styling: ThemeManager
Assets: ui/resources
```

Thiet ke hien tai phu hop cho giai doan dau cua ung dung desktop: de doc, de mo rong va da co su tach biet co ban giua giao dien, dieu huong, service va theme.
