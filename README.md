# Hand Tracking & Gesture Recognition (MediaPipe)

Project nhỏ làm **cho vui / học tập**, sử dụng **MediaPipe + OpenCV** để:

* Phát hiện bàn tay realtime qua webcam
* Vẽ 21 landmarks của bàn tay
* Nhận diện một số **gesture cơ bản (rule-based, không train)**

---

## ✋ Các gesture hiện có

* **FIST** ✊ – Nắm tay
* **OPEN PALM** ✋ – Bàn tay mở
* **THUMB UP** 👍 – Ngón cái hướng lên
* **PEACE** ✌️ – Ngón trỏ + ngón giữa

> Lưu ý: Đây là **gesture recognition đơn giản**, không phải sign language đầy đủ.

---

## 🛠 Công nghệ sử dụng

* **Python 3.9**
* **MediaPipe** (Hand Tracking)
* **OpenCV** (Webcam & hiển thị)

---

## ⚙️ Cài đặt môi trường

### 1. Cài Python 3.9

Tải tại: [https://www.python.org/downloads/release/python-390/](https://www.python.org/downloads/release/python-390/)

> Khi cài nhớ tick **Add Python to PATH**

---

### 2. Tạo virtual environment

```bash
py -3.9 -m venv venv
```

Kích hoạt (Windows PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

Kiểm tra:

```bash
python --version
# Python 3.9.x
```

---

### 3. Cài thư viện cần thiết

```bash
pip install opencv-python mediapipe==0.10.9
```

---

## ▶️ Chạy chương trình

```bash
python hand_tracker.py
```

* Nhấn **ESC** để thoát
* Đảm bảo webcam không bị app khác chiếm

---

## 🧠 Ý tưởng hoạt động

1. OpenCV đọc frame từ webcam
2. MediaPipe detect bàn tay và trả về **21 landmarks**
3. So sánh vị trí các khớp để xác định **ngón tay duỗi / gập**
4. Áp dụng **rule-based logic** để suy ra gesture

---

## 📌 Cấu trúc thư mục

```
hand-tracking/
│── hand_tracker.py
│── README.md
│── venv/
```

---

## ⚠️ Lưu ý quan trọng

* Mỗi lần mở terminal mới cần **activate venv**
* MediaPipe **chưa support Python 3.11+**
* Gesture có thể nhiễu nếu ánh sáng kém hoặc xoay tay mạnh

---
---

✌️ Have fun với Hand Tracking!
