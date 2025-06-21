# upload_to_youtube.py

import os
import random
import subprocess
from config import OUTPUT_VIDEO, KEYWORDS

def buat_judul():
    hook = random.choice(KEYWORDS)
    judul = f"{hook} bikin ngakak #upinipin #tungtungtungsahur #funny #lucu #short #dontol"
    return judul[:95]  # YouTube Shorts title limit

def upload_video():
    if not os.path.exists(OUTPUT_VIDEO):
        print("❌ Video belum ditemukan. Jalankan make_video.py dulu.")
        return

    judul = buat_judul()

    cmd = [
        "youtube-upload",
        "--title", judul,
        "--privacy", "public",
        "--shorts",
        OUTPUT_VIDEO
    ]

    print("📤 Mengupload video...")
    subprocess.run(cmd)
    print("✅ Video berhasil diupload!")

if __name__ == "__main__":
    upload_video()
