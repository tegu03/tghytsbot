# generate_story.py

import random
import requests
import json
from datetime import datetime

from config import KARAKTER_LIST

def generate_prompt(karakter):
    return f"Buat cerita absurd dan lucu dalam 3 kalimat tentang {karakter} yang mengalami kejadian aneh dan tidak masuk akal."

def generate_story(prompt):
    # API gratis dari textsynth.com
    url = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.9,
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        data = response.json()
        return data.get("text", "").strip()
    except Exception as e:
        return f"Cerita gagal dibuat: {e}"

def simpan_ke_file(karakter, cerita):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"cerita/cerita_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Karakter: {karakter}\n")
        f.write(f"{cerita}")
    return filename

if __name__ == "__main__":
    karakter = random.choice(KARAKTER_LIST)
    prompt = generate_prompt(karakter)
    cerita = generate_story(prompt)
    file_path = simpan_ke_file(karakter, cerita)

    print(f"Cerita disimpan di: {file_path}")

