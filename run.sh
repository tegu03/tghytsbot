# run.sh

#!/data/data/com.termux/files/usr/bin/bash

# Jalankan semua tahapan otomatis

echo "📚 Generate cerita..."
python generate_story.py

echo "🎨 Gabungkan gambar..."
python compose_image.py

echo "🎵 Ambil audio dari playlist..."
python fetch_audio.py

echo "🎬 Buat video..."
python make_video.py

echo "📤 Upload ke YouTube Shorts..."
python upload_to_youtube.py
