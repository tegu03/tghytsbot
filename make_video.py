# make_video.py

import os
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
from config import OUTPUT_IMAGE, OUTPUT_AUDIO, OUTPUT_VIDEO, MAX_DURATION

def buat_video():
    if not os.path.exists(OUTPUT_IMAGE):
        print("❌ Gambar belum dibuat. Jalankan compose_image.py dulu.")
        return
    if not os.path.exists(OUTPUT_AUDIO):
        print("❌ Audio belum tersedia. Jalankan fetch_audio.py dulu.")
        return

    gambar = ImageClip(OUTPUT_IMAGE).set_duration(MAX_DURATION)
    audio = AudioFileClip(OUTPUT_AUDIO).subclip(0, MAX_DURATION)

    video = CompositeVideoClip([gambar.set_audio(audio)])
    os.makedirs("output", exist_ok=True)
    video.write_videofile(OUTPUT_VIDEO, fps=24)
    print(f"✅ Video berhasil disimpan ke {OUTPUT_VIDEO}")

if __name__ == "__main__":
    buat_video()
