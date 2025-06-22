# ✅ FIXED FINAL VERSION — generate_story.py
import os
from datetime import datetime
import random

OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

karakter_list = [
    "upin", "ipin", "mail", "ehsan", "mei-mei",
    "kak_ros", "tok_dalang", "jarjit", "dontol", "tung_tung_sahur"
]

latar = [
    "di pasar malam", "di kebun durian", "di sekolah", "di rumah tok dalang",
    "di jalan misterius", "di hutan larangan"
]

alur = [
    "menemukan benda aneh", "bertemu hantu lucu", "tersesat dan bertemu alien",
    "berubah jadi zombie", "terjebak dalam game", "mendapat kekuatan super"
]

def buat_cerita(karakter):
    lokasi = random.choice(latar)
    kejadian = random.choice(alur)
    return f"Pada suatu hari, {karakter} bermain bersama teman-temannya {lokasi}. Tanpa diduga, mereka {kejadian}."

def simpan_ke_file(karakter, cerita):
    filename = f"{OUTPUT_FOLDER}/cerita.txt"
    with open(filename, "w") as f:
        f.write(f"[Karakter Utama: {karakter}]\n")
        f.write(cerita)
    return filename

karakter = random.choice(karakter_list)
cerita = buat_cerita(karakter)
file_path = simpan_ke_file(karakter, cerita)

print(f"✅ Cerita disimpan di: {file_path}")
