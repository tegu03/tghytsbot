# fetch_audio.py

import os
import random
import subprocess
from config import PLAYLIST_URL, OUTPUT_AUDIO

def unduh_audio():
    os.makedirs("temp_audio", exist_ok=True)
    print("🎵 Mengambil audio dari playlist...")

    # Ambil daftar video dari playlist
    list_cmd = [
        "yt-dlp", "--flat-playlist", "--print", "%(id)s", PLAYLIST_URL
    ]
    result = subprocess.run(list_cmd, stdout=subprocess.PIPE, text=True)
    video_ids = result.stdout.strip().split("\n")

    if not video_ids:
        print("❌ Tidak ditemukan video dalam playlist.")
        return

    video_id = random.choice(video_ids)
    url = f"https://www.youtube.com/watch?v={video_id}"

    # Unduh audio
    audio_cmd = [
        "yt-dlp", "-f", "bestaudio", "--extract-audio",
        "--audio-format", "mp3", "-o", "temp_audio/audio.%(ext)s", url
    ]
    subprocess.run(audio_cmd)

    if not os.path.exists("temp_audio/audio.mp3"):
        print("❌ Gagal mengunduh audio.")
        return

    os.rename("temp_audio/audio.mp3", OUTPUT_AUDIO)
    print(f"✅ Audio disimpan sebagai {OUTPUT_AUDIO}")

if __name__ == "__main__":
    unduh_audio()
