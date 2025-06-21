# config.py

# Link playlist YouTube (isi dengan ID playlist kamu)
PLAYLIST_URL = "https://www.youtube.com/playlist?list=SS"

# Daftar karakter (nama file tanpa .png) yang ada di folder assets/karakter/
KARAKTER_LIST = [
    "upin",
    "ipin",
    "tok_dalang",
    "ah_tong",
    "angkel_muthu",
    "opah",
    "dontol",
    "tung_tung_sahur"
    "mail"
    "kak_ros"
]

# Kata kunci hook & hashtag yang digunakan di judul dan deskripsi video
KEYWORDS = [
    "UPIN IPIN", "DONTOL", "Tung Tung Sahur", "Ah Tong",
    "Tok Dalang", "Angkel Muthu", "Opah"
]

# Hashtag tetap
HASHTAGS = [
    "#upinipin", "#tungtungtungsahur", "#funny", "#lucu", "#short", "#dontol"
]

# Path font untuk teks overlay
FONT_PATH = "assets/font.ttf"

# Durasi maksimal video dalam detik
MAX_DURATION = 15

# Ukuran output gambar/video
RESOLUTION = (1080, 1920)  # Format 9:16

# Folder output
OUTPUT_IMAGE = "output/frame.png"
OUTPUT_VIDEO = "output/video.mp4"
OUTPUT_TEXT = "output/cerita.txt"

# OpenAI API
USE_OPENAI = True
OPENAI_MODEL = "gpt-4"

# Format jadwal upload otomatis (WIB, jam 7, 11, 17, 22)
UPLOAD_TIMES = ["07:00", "11:00", "17:00", "22:00"]
