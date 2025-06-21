#!/data/data/com.termux/files/usr/bin/bash

echo "🕗 Menjalankan bot YouTube Shorts $(date)"

# 1. Generate cerita absurd
echo "📚 Membuat cerita..."
python generate_story.py

# 2. Gabungkan gambar karakter
echo "🎨 Menggabungkan gambar..."
python compose_image.py

# 3. Download audio dari playlist jika belum ada
echo "🎵 Cek & ambil audio dari playlist..."
yt-dlp -x --audio-format mp3 --playlist-items 1 -o "sounds/sound_%(upload_date)s.%(ext)s" "$(python3 -c 'import config; print(config.PLAYLIST_URL)')"

# 4. Buat video dari gambar + teks + sound
echo "🎬 Membuat video..."
python make_video.py

# 5. Upload ke YouTube Shorts
echo "📤 Upload ke YouTube..."
python upload_video.py

echo "✅ Selesai: $(date)"

