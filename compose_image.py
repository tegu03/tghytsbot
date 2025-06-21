# compose_image.py

from PIL import Image, ImageDraw, ImageFont
import os
from config import KARAKTER_LIST, RESOLUTION, FONT_PATH, OUTPUT_IMAGE, OUTPUT_TEXT

def gabungkan_gambar_karakter(karakter_list, ukuran=(1080, 1920)):
    canvas = Image.new("RGB", ukuran, (255, 255, 255))
    lebar, tinggi = ukuran
    total = len(karakter_list)
    ukuran_karakter = lebar // total

    for i, nama in enumerate(karakter_list):
        path = f"assets/karakter/{nama}.png"
        if not os.path.exists(path):
            print(f"⚠️ Gambar {path} tidak ditemukan")
            continue
        gambar = Image.open(path).convert("RGBA")
        gambar = gambar.resize((ukuran_karakter, int(ukuran_karakter * 1.5)))
        posisi = (i * ukuran_karakter, tinggi - gambar.height)
        canvas.paste(gambar, posisi, gambar)

    return canvas

def tambahkan_teks(cerita, gambar):
    draw = ImageDraw.Draw(gambar)
    font = ImageFont.truetype(FONT_PATH, 48)

    baris = cerita.split("\n")
    y = 30
    for line in baris:
        draw.text((30, y), line, font=font, fill=(0, 0, 0))
        y += 60
    return gambar

def baca_karakter_dari_cerita():
    with open(OUTPUT_TEXT, "r") as f:
        baris = f.readline()
        karakter = baris.replace("[Karakter Utama: ", "").replace("]", "").strip()
    return karakter

def baca_cerita():
    with open(OUTPUT_TEXT, "r") as f:
        cerita = f.read().split("\n", 1)[-1].strip()
    return cerita

def buat_frame():
    karakter_utama = baca_karakter_dari_cerita()
    cerita = baca_cerita()
    karakter_lain = list(set(KARAKTER_LIST) - {karakter_utama})
    karakter_acak = [karakter_utama] + karakter_lain[:2]

    gambar = gabungkan_gambar_karakter(karakter_acak)
    gambar = tambahkan_teks(cerita, gambar)

    os.makedirs("output", exist_ok=True)
    gambar.save(OUTPUT_IMAGE)
    print(f"✅ Gambar disimpan ke {OUTPUT_IMAGE}")

if __name__ == "__main__":
    buat_frame()
