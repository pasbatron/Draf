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





