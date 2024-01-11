pip install Pillow keyboard


import os
import keyboard
from PIL import ImageGrab

def ambil_gambar():
    # Mengambil tangkapan layar
    screenshot = ImageGrab.grab()

    # Menyimpan gambar di direktori D:\ dengan nama file yang unik
    path = "D:\\"
    filename = "screenshot.png"
    full_path = os.path.join(path, filename)
    screenshot.save(full_path)
    print(f"Gambar disimpan di: {full_path}")

def main():
    print("Program Pengambil Gambar (Tekan Enter untuk Mengambil Gambar, Tekan 'q' untuk Keluar)")

    while True:
        # Menunggu tombol Enter atau 'q' ditekan
        key = keyboard.read_event(suppress=True).name

        if key == "enter":
            ambil_gambar()
        elif key == "q":
            print("Program dihentikan.")
            break

if __name__ == "__main__":
    main()









pip install opencv-python-headless keyboard

import os
import cv2
import keyboard
from datetime import datetime

def ambil_gambar():
    # Mengambil gambar dari kamera (webcam)
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()

    # Mendapatkan tanggal dan waktu saat ini
    waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S")

    # Menyimpan gambar di direktori home dengan nama file yang mengandung tanggal dan waktu
    path = os.path.expanduser("~")
    filename = f"snapshot_{waktu_sekarang}.png"
    full_path = os.path.join(path, filename)
    cv2.imwrite(full_path, frame)
    print(f"Gambar disimpan di: {full_path}")

    # Menutup kamera
    cap.release()

def main():
    print("Program Pengambil Gambar (Tekan Enter untuk Mengambil Gambar, Tekan 'q' untuk Keluar)")

    while True:
        # Menunggu tombol Enter atau 'q' ditekan
        key = keyboard.read_event(suppress=True).name

        if key == "enter":
            ambil_gambar()
        elif key == "q":
            print("Program dihentikan.")
            break

if __name__ == "__main__":
    main()









