# compose_image.py

from PIL import Image
import random
import os
from config import KARAKTER_LIST

def pilih_karakter():
    karakter_utama = random.choice(KARAKTER_LIST)
    karakter_lain = random.sample([k for k in KARAKTER_LIST if k != karakter_utama], 2)
    return karakter_utama, karakter_lain

def buat_frame(karakter_utama, karakter_lain):
    # Buat canvas kosong ukuran 9:16 (1080x1920)
    canvas = Image.new("RGB", (1080, 1920), (255, 255, 255))  # Background putih

    posisi = [(100, 1100), (600, 1100), (350, 400)]  # Posisi karakter
    semua_karakter = karakter_lain + [karakter_utama]
    random.shuffle(posisi)

    for idx, nama in enumerate(semua_karakter):
        path_gambar = f"karakter/{nama}.png"
        if os.path.exists(path_gambar):
            img = Image.open(path_gambar).convert("RGBA")
            img = img.resize((400, 400))  # Ubah ukuran standar
            canvas.paste(img, posisi[idx], img)
        else:
            print(f"Gambar tidak ditemukan: {path_gambar}")

    nama_file = f"video/frame_{karakter_utama}.png"
    canvas.save(nama_file)
    return nama_file, karakter_utama

if __name__ == "__main__":
    utama, lainnya = pilih_karakter()
    output, _ = buat_frame(utama, lainnya)
    print(f"Frame disimpan di: {output}")

