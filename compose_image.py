# compose_image.py
import os
from PIL import Image
from datetime import datetime

OUTPUT_TEXT = "output/cerita.txt"
KARAKTER_FOLDER = "karakter"
OUTPUT_IMAGE = f"video/frame_{datetime.now().strftime('%Y%m%d_%H%M')}.jpg"

os.makedirs("video", exist_ok=True)

def baca_karakter_dari_cerita():
    with open(OUTPUT_TEXT, "r") as f:
        line = f.readline()
        if "[Karakter Utama:" in line:
            return line.strip().split(":")[1].replace("]", "").strip()
    return "upin"

def gabungkan_gambar(gambar_list):
    gambar_utama = Image.open(gambar_list[0]).resize((720, 1280))
    canvas = Image.new("RGB", (720, 1280), (255, 255, 255))
    canvas.paste(gambar_utama, (0, 0))

    for i, path in enumerate(gambar_list[1:]):
        img = Image.open(path).resize((200, 200))
        canvas.paste(img, (50 + i*220, 1000))

    canvas.save(OUTPUT_IMAGE)
    return OUTPUT_IMAGE

def buat_frame():
    karakter_utama = baca_karakter_dari_cerita()
    try:
        utama_path = os.path.join(KARAKTER_FOLDER, f"{karakter_utama}.jpg")
        lainnya = [f for f in os.listdir(KARAKTER_FOLDER) if f.endswith(".jpg") and not f.startswith(karakter_utama)]
        lainnya_paths = [os.path.join(KARAKTER_FOLDER, f) for f in lainnya[:2]]

        if not os.path.exists(utama_path):
            raise FileNotFoundError(f"Gambar tidak ditemukan: {utama_path}")

        all_paths = [utama_path] + lainnya_paths
        hasil = gabungkan_gambar(all_paths)
        print(f"✅ Frame disimpan di: {hasil}")
    except Exception as e:
        print(f"❌ Gagal membuat frame: {e}")

if __name__ == "__main__":
    buat_frame()
