# make_video.py

import os
import random
from datetime import datetime
import subprocess
from config import FONT_PATH, MAX_DURATION

def ambil_terbaru(folder, ekstensi):
    file_list = [f for f in os.listdir(folder) if f.endswith(ekstensi)]
    if not file_list:
        return None
    file_list.sort()
    return os.path.join(folder, file_list[-1])

def buat_video():
    gambar = ambil_terbaru("video", ".png")
    cerita = ambil_terbaru("cerita", ".txt")
    sound = ambil_terbaru("sounds", ".mp3")

    if not all([gambar, cerita, sound]):
        print("❌ File belum lengkap (gambar/cerita/sound)")
        return None

    # Baca isi cerita
    with open(cerita, "r") as f:
        lines = f.readlines()
        teks = "".join(lines[1:]).replace("\n", " ")

    # Buat file teks sementara untuk ffmpeg
    with open("teks_overlay.txt", "w") as f:
        f.write(teks)

    output_file = f"video/final_{datetime.now().strftime('%Y%m%d_%H%M')}.mp4"

    # ffmpeg command
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", gambar,
        "-i", sound,
        "-vf", f"drawtext=textfile=teks_overlay.txt:fontfile={FONT_PATH}:fontsize=40:fontcolor=white:x=20:y=H-th-80",
        "-t", str(random.randint(10, MAX_DURATION)),
        "-pix_fmt", "yuv420p",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Video berhasil dibuat: {output_file}")
        return output_file
    except subprocess.CalledProcessError:
        print("❌ Gagal membuat video")
        return None

if __name__ == "__main__":
    buat_video()

