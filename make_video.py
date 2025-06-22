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

    try:
        gambar = ImageClip(OUTPUT_IMAGE).set_duration(MAX_DURATION)
    except Exception as e:
        print(f"❌ Gagal memuat gambar: {e}")
        return

    try:
        audio = AudioFileClip(OUTPUT_AUDIO).subclip(0, MAX_DURATION)
    except Exception as e:
        print(f"❌ Gagal memuat audio: {e}")
        return

    try:
        video = CompositeVideoClip([gambar.set_audio(audio)])
        os.makedirs(os.path.dirname(OUTPUT_VIDEO), exist_ok=True)
        video.write_videofile(OUTPUT_VIDEO, fps=24)
        print(f"✅ Video berhasil disimpan ke {OUTPUT_VIDEO}")
    except Exception as e:
        print(f"❌ Gagal membuat video: {e}")

if __name__ == "__main__":
    buat_video()
