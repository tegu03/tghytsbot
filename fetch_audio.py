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
    result = subprocess.run(list_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print("❌ Gagal mengambil daftar video. Pastikan playlist URL benar.")
        print(result.stderr)
        return

    video_ids = result.stdout.strip().split("\n")

    if not video_ids or not video_ids[0].strip():
        print("❌ Tidak ditemukan video dalam playlist.")
        return

    video_id = random.choice(video_ids)
    url = f"https://www.youtube.com/watch?v={video_id}"

    print(f"🎧 Mengunduh audio dari: {url}")

    # Unduh audio dari video
    audio_cmd = [
        "yt-dlp", "-f", "bestaudio", "--extract-audio",
        "--audio-format", "mp3", "-o", "temp_audio/audio.%(ext)s", url
    ]
    subprocess.run(audio_cmd)

    source_path = "temp_audio/audio.mp3"
    if not os.path.exists(source_path):
        print("❌ Gagal mengunduh audio.")
        return

    os.makedirs(os.path.dirname(OUTPUT_AUDIO), exist_ok=True)
    os.rename(source_path, OUTPUT_AUDIO)
    print(f"✅ Audio disimpan sebagai: {OUTPUT_AUDIO}")

if __name__ == "__main__":
    unduh_audio()
