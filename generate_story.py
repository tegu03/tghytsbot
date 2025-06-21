# generate_story.py

import random
import openai
import os
from datetime import datetime
from config import KARAKTER_LIST, KEYWORDS, OUTPUT_TEXT
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ambil karakter utama secara acak
def pilih_karakter():
    return random.choice(KARAKTER_LIST)

# Ambil keyword untuk hook
def buat_judul_acak():
    return random.choice(KEYWORDS)

# Generate cerita absurd dari GPT
def generate_story(karakter):
    prompt = f"Buatkan cerita absurd, lucu, dan pendek dalam 5 kalimat dengan karakter utama bernama {karakter}. Cerita harus cocok untuk video YouTube Shorts, dengan gaya komedi random dan tidak masuk akal."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Kamu adalah penulis cerita pendek absurd lucu."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Simpan cerita ke file
def simpan_ke_file(karakter, cerita):
    now = datetime.now().strftime("%Y%m%d_%H%M")
    os.makedirs("output", exist_ok=True)
    filename = OUTPUT_TEXT
    with open(filename, "w") as f:
        f.write(f"[Karakter Utama: {karakter}]
")
        f.write(cerita + "\n")
    print(f"✅ Cerita disimpan ke {filename}")
    return filename

if __name__ == "__main__":
    karakter = pilih_karakter()
    cerita = generate_story(karakter)
    simpan_ke_file(karakter, cerita)
