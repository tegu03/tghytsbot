# upload_video.py

import os
import random
import shlex
from datetime import datetime
import subprocess
from config import KEYWORDS

HASHTAGS = "#upinipin #tungtungtungsahur #funny #lucu #short #dontol"

def ambil_terbaru(folder, ekstensi):
    file_list = [f for f in os.listdir(folder) if f.endswith(ekstensi)]
    if not file_list:
        return None
    file_list.sort()
    return os.path.join(folder, file_list[-1])

def buat_judul():
    hook = random.choice([
        "GILA SIH INI!",
        "INI NGAKAK PARAH!",
        "KAMU NGGAK AKAN PERCAYA!",
        "PLOT TWIST LUCU!",
        "ASTAGA DONTOLNYA APAKAH..."
    ])
    keyword = random.choice(KEYWORDS)
    # Bungkus judul dengan kutip satu agar aman dari Bash expansion
    judul = f"{hook} {keyword} {HASHTAGS}"
    return judul

def upload_ke_youtube(video_path, judul):
    if not video_path:
        print("❌ Video tidak ditemukan")
        return

    cmd = [
        "youtube-upload",
        "--title", judul,
        "--description", "Video absurd & lucu otomatis setiap hari!",
        "--privacy", "public",
        video_path
    ]

    # Gunakan shell=False agar aman dari karakter spesial seperti '!'
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Video di-upload: {judul}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Gagal upload: {e}")

if __name__ == "__main__":
    video = ambil_terbaru("video", ".mp4")
    judul = buat_judul()
    upload_ke_youtube(video, judul)

