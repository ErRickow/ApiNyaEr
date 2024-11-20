

---

# 📘 API Documentation

Welcome to the **ErApi**! This library allows you to easily interact with the API using both **synchronous** and **asynchronous** options.

- **Sync**: `from ApiNyaEr.sync import apinya`
- **Async**: `from ApiNyaEr import apinya`

Below, we’ll cover each function, providing examples and expected results so you can get started quickly! Let’s dive in 🚀

## Status

| Function           | Status |
|--------------------|--------|
| [1. Ai](#1-ai) | ✅
| [2. Bing Image](#2-bing-image) | ✅
| [3. Blackbox](#3-blackbox) | ✅
| [4. Carbon](#4-carbon) | ✅
| [5. Cat](#5-cat) | ✅
| [6. Dare](#6-dare) | ✅
| [7. Doa](#7-doa) | ✅
| [8. Dog](#8-dog) | ✅
| [9. Fakta Unik](#9-fakta-unik) | ✅
| [10. Gemini](#10-gemini) | ✅
| [11. Github Search](#11-github-search) | ✅
| [12. Hug](#12-hug) | ✅
| [13. Kapan Libur](#13-kapan-libur) | ✅
| [14. Nama Epep](#14-nama-epep) | ✅
| [15. Password](#15-password) | ✅
| [16. Pypi](#16-pypi) | ❌
| [17. Qanime](#17-qanime) | ✅
| [18. Qhacker](#18-qhacker) | ✅
| [19. Qislam](#19-qislam) | ✅
| [20. Qpubg](#20-qpubg) | ✅
| [21. Truth](#21-truth) | ✅
| [22. Wibu](#22-wibu) | ✅


## 🎓 How to Use Each Function

### 1. Ai

**Description**:
Interaksi dengan AI Basis Text.

**Args:**
**Description**:
tanya (str): Text inputnya.

**Returns:**
**Description**:
str: Respon chatbotnya.

```python
from ApiNyaEr import apinya

result = await apinya.ai(tanya='Tidur')
print(result)
```

#### Expected Output

```text
Kenapa nak tidur.
```

### 2. Bing Image

**Description**:
Cari bing images based om teks.

**Args:**
  - **teks (str)**: Teks quesy yang ingin di cari gambarnya.
  - **limit (int, optional)**: Maximum number photonya. Defaults nya 1.

**Returns:**
  - **list**: List image url yang di terima.

```python
from ApiNyaEr import apinya

result = await apinya.bing_image(teks='Tidur', limit=1)
print(result)
```

#### Expected Output

```text
https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/14044059/Kenali-Pola-Tidur-yang-Baik-untuk-Kesehatan.jpg
```

### 3. Blackbox

**Description**:
Berinteraksi dengan Blackbox AI untuk menghasilkan konten. 🧠

**Args:**
  - **tanya (str)**: Teks masukan untuk berinteraksi dengan API obrolan Blackbox AI.

**Returns:**
  - **requests.Response**: Objek respons dari permintaan API.

```python
from ApiNyaEr import apinya

result = await apinya.blackbox(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "results": "",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 4. Carbon

**Args:**
  - **query (str)**: Potongan kode yang akan dirender sebagai gambar.

**Description**:
Return: FilePath: Jalur file dari gambar yang disimpan.

```python
from ApiNyaEr import apinya

result = await apinya.carbon(query='Tidur')
print(result)
```

#### Expected Output

```text
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_6ZWxRfYx.png
```

### 5. Cat

**Description**:
Generate random gambar kucing.

**Returns:**
  - **str or None**: Url random kucing ataupun None; None jika response
    tidak di terima.

```python
from ApiNyaEr import apinya

result = await apinya.cat()
print(result)
```

#### Expected Output

```text
https://cdn2.thecatapi.com/images/267.jpg
```

### 6. Dare

**Description**:
Dapatkan Kata kata dare

**Returns:**
  - **str**: Random kata dare

```python
from ApiNyaEr import apinya

result = await apinya.dare()
print(result)
```

#### Expected Output

```text
Bilang pada seseorang di kelas, 'Aku baru saja diberi tahu aku adalah kembaranmu dulu, kita dipisahkan, lalu aku menjalani operasi plastik. Dan ini adalah hal paling serius yang pernah aku katakan.'
```

### 7. Doa

**Description**:
Mengambil data doa dari API ItzPire berdasarkan nama doa.

**Args:**
  - **nama_doa (str)**: Nama doa yang ingin diambil.

**Returns:**
  - **str**: Teks doa yang diformat dengan rapi termasuk doa, ayat, latin, dan artinya.

```python
from ApiNyaEr import apinya

result = await apinya.doa(nama_doa='Tidur')
print(result)
```

#### Expected Output

```text
Doa sebelum tidur
Ayat: بِسْمِكَ االلّٰهُمَّ اَحْيَا وَبِاسْمِكَ اَمُوْتُ
Latin: Bismikallaahumma ahyaa wa ammuut
Artinya: Dengan menyebut nama Allah, aku hidup dan aku mati
```

### 8. Dog

**Description**:
Dapatkan random foto anjing.

**Returns:**
  - **str or None**: Url Random anjing jika tersedia; None jika tidak ada
    response yang di terima.

```python
from ApiNyaEr import apinya

result = await apinya.dog()
print(result)
```

#### Expected Output

```text
https://random.dog/c2e5058f-fd49-4bf9-89c8-e05dee5fb7bc.mp4
```

### 9. Fakta Unik

**Description**:
Dapatkan random Seputar Fakta Unik

**Returns:**
  - **str**: Random Fakta

```python
from ApiNyaEr import apinya

result = await apinya.fakta_unik()
print(result)
```

#### Expected Output

```text
🌾 **IBM mengatakan bahwa dalam kurun waktu 5 tahun ke depan, komputer bakal mirip manusia yang bisa melihat, mendengar, mencium dan merasakan.**
```

### 10. Gemini

**Description**:
Berinteraksi dengan Gemini AI. ✨

**Args:**
  - **tanya (str)**: Teks yang di berikan.

**Returns:**
  - **dict**: dictionaries yang berisi konten ai nya.

```python
from ApiNyaEr import apinya

result = await apinya.gemini(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "results": "**Proses Tidur**\n\nTidur adalah keadaan relaksasi yang berulang dan dapat diubah, di mana terjadi hilangnya kesadaran secara parsial. Ini adalah proses penting yang diperlukan untuk kesehatan fisik, emosional, dan kognitif.\n\nTidur umumnya terdiri dari dua fase utama:\n\n* **Tidur Non-REM (Tidur Nyata)**\n\nTidur non-REM dibagi lagi menjadi tiga tahap:\n\n    * **Tahap 1:** Tidur yang sangat ringan. Mata bergerak perlahan dan otot-otot rileks.\n    * **Tahap 2:** Tidur yang lebih dalam. Mata berhenti bergerak dan gelombang otak mulai melambat.\n    * **Tahap 3:** Tidur nyenyak yang ditandai dengan gelombang otak yang sangat lambat.\n\n* **Tidur REM (Tidur Gerak Mata Cepat)**\n\nTidur REM ditandai dengan:\n\n    * Mata bergerak cepat ke segala arah.\n    * Otot-otot hampir lumpuh.\n    * Mimpi yang intens.\n    * Peningkatan detak jantung dan pernapasan.\n\n**Manfaat Tidur**\n\nTidur yang cukup sangat penting untuk kesehatan secara keseluruhan, antara lain:\n\n* **Kesehatan fisik:** Memperbaiki fungsi kekebalan tubuh, mengatur metabolisme, dan mengurangi risiko penyakit kronis.\n* **Kesehatan emosional:** Mengurangi stres, kecemasan, dan depresi.\n* **Kesehatan kognitif:** Meningkatkan memori, konsentrasi, dan fungsi eksekutif.\n* **Kesejahteraan:** Meningkatkan suasana hati, energi, dan kualitas hidup secara keseluruhan.\n\n**Durasi Tidur yang Disarankan**\n\nJumlah tidur yang direkomendasikan bervariasi sesuai usia:\n\n* Bayi baru lahir: 14-17 jam per hari\n* Anak-anak usia prasekolah: 11-14 jam per hari\n* Anak-anak usia sekolah: 9-11 jam per hari\n* Remaja: 8-10 jam per hari\n* Dewasa muda: 7-9 jam per hari\n* Orang dewasa yang lebih tua: 7-8 jam per hari\n\n**Tips untuk Meningkatkan Kualitas Tidur**\n\n* Tetapkan jadwal tidur yang teratur dan patuhilah setiap hari, bahkan di akhir pekan.\n* Ciptakan lingkungan tidur yang sejuk, gelap, dan tenang.\n* Hindari kafein dan alkohol sebelum tidur.\n* Lakukan aktivitas santai sebelum tidur, seperti membaca, mandi air hangat, atau mendengarkan musik yang menenangkan.\n* Pastikan Anda mendapatkan cukup sinar matahari di siang hari.\n* Hindari penggunaan perangkat elektronik setidaknya satu jam sebelum tidur.\n* Jika Anda tidak bisa tidur setelah 20 menit, bangunlah dan lakukan sesuatu yang menenangkan sampai Anda merasa mengantuk.\n* Konsultasikan dengan dokter jika Anda mengalami masalah tidur berkelanjutan.",
    "author": "@chakszzz",
    "success": true
}
```

### 11. Github Search

**Description**:
Pencarian GitHub untuk beberapa tipe konten.

**Args:**
  - **cari (str)**: untuk Pencarian.
  - **tipe (str, optional)**: Type pencarian, terdiri dari:
    - "repositories"
    - "users"
    - "organizations"
    - "issues"
    - "pull_requests"
    - "commits"
    - "topics"

**Description**:
Defaults ke "repositories". max_results (int, optional): Maximum nomor dari results untuk return. Defaultnya 3.

**Returns:**
  - **list**: List dari pencarian results atau pesan error.

```python
from ApiNyaEr import apinya

result = await apinya.github_search(cari='Tidur', tipe='repositories', max_results=3)
print(result)
```

#### Expected Output

```json
[
    {
        "name": "rs-bed-covid-indo-api",
        "full_name": "satyawikananda/rs-bed-covid-indo-api",
        "description": "API ketersediaan rumah sakit dan tempat tidur rumah sakit untuk pasien covid-19 ataupun non-covid yang berada di Indonesia",
        "url": "https://github.com/satyawikananda/rs-bed-covid-indo-api",
        "language": "TypeScript",
        "stargazers_count": 112,
        "forks_count": 25
    },
    {
        "name": "bed-covid-rs-indo",
        "full_name": "hendraaagil/bed-covid-rs-indo",
        "description": "Website yang memberikan informasi terkait ketersediaan rumah sakit dan tempat tidur rumah sakit untuk pasien covid-19 ataupun non-covid di Indonesia.",
        "url": "https://github.com/hendraaagil/bed-covid-rs-indo",
        "language": "JavaScript",
        "stargazers_count": 23,
        "forks_count": 3
    },
    {
        "name": "hobikoding.github.io",
        "full_name": "hobikoding/hobikoding.github.io",
        "description": ":rose: Hobikoding - Mari ngoding sambil tidur",
        "url": "https://github.com/hobikoding/hobikoding.github.io",
        "language": "Makefile",
        "stargazers_count": 3,
        "forks_count": 0
    }
]
```

### 12. Hug

**Description**:
Dapatkan gif Random pelukan dari Nekos.Best API.

**Args:**
  - **amount (int)**: amount gambar nya, Defaultnya 1.

**Returns:**
  - **list**: List dari dictionaries tentang informasi neko image atau GIF.
    Type dictionaries:
    - anime_name (str): Nama anime.
    - url (str): Url gif nya.

```python
from ApiNyaEr import apinya

result = await apinya.hug(amount=1)
print(result)
```

#### Expected Output

```json
[
    {
        "anime_name": "Akatsuki no Yona: The Girl Standing in the Blush of Dawn",
        "url": "https://nekos.best/api/v2/hug/2838c749-cbf0-407c-b727-ceb1ca517463.gif"
    }
]
```

### 13. Kapan Libur

**Description**:
Dapatkan informasi Hari libur kedepan.

**Returns:**
  - **str**: Hari Libur Berikutnya.

```python
from ApiNyaEr import apinya

result = await apinya.kapan_libur()
print(result)
```

#### Expected Output

```text
Hari liburberikutnya adalah Hari Natal yang jatuh di hari Rabu, 25 Desember 2024 (35 hari lagi)
```

### 14. Nama Epep

**Description**:
Dapatkan random nama ep ep

**Returns:**
  - **str**: Random nama ep epnya

```python
from ApiNyaEr import apinya

result = await apinya.nama_epep()
print(result)
```

#### Expected Output

```text
ρнχ•乙ᴮᴬᴰʙᴏʏ乂
```

### 15. Password

**Description**:
Fungsi ini menghasilkan kata sandi acak dengan menggabungkan huruf besar, huruf kecil, tanda baca, dan digit.

**Description**:
Parameters: - num (int): Panjang kata sandi yang dihasilkan. Default adalah 12 jika tidak ditentukan.

**Returns:**
**Description**:
- str: Kata sandi yang dihasilkan secara acak yang terdiri dari karakter dari string.ascii_letters, string.punctuation, dan string.digits.

```python
from ApiNyaEr import apinya

result = await apinya.password(num=12)
print(result)
```

#### Expected Output

```text
$W9CM<Y/#h+a
```

### 16. Pypi

**Description**:
Mengambil informasi metadata tentang paket Python tertentu dari API PyPI.

**Args:**
  - **namanya (str)**: Nama paket yang dicari di PyPI.

**Returns:**
  - **dict atau None**: Sebuah kamus dengan informasi relevan tentang paket jika ditemukan, yang berisi:
    - name (str): Nama paket.
    - version (str): Versi terbaru paket.
    - summary (str): Deskripsi singkat tentang paket.
    - author (str): Penulis paket.
    - author_email (str): Email penulis paket.
    - license (str): Jenis lisensi.
    - home_page (str): URL halaman utama paket.
    - package_url (str): URL paket di PyPI.
    - requires_python (str): Versi Python minimum yang dibutuhkan.
    - keywords (str): Kata kunci yang terkait dengan paket.
    - classifiers (list): Daftar pengklasifikasi PyPI.
    - project_urls (dict): URL proyek tambahan (misalnya, kode sumber, dokumentasi).
**Description**:
Returns None jika paket tidak ditemukan atau terjadi kesalahan.

```python
from ApiNyaEr import apinya

result = await apinya.pypi(namanya='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 404, message='Not Found', url='https://pypi.org/pypi/Tidur/json'
```

### 17. Qanime

**Description**:
Dapatkan Kata kata anime

**Returns:**
  - **str**: Random kata anime

```python
from ApiNyaEr import apinya

result = await apinya.qanime()
print(result)
```

#### Expected Output

```json
{
    "\ud83c\udf81 **Quotes": "Kata-kata dapat menyakiti seseorang. Meskipun kau menyesalinya, kau takkan pernah bisa menarik kembali (kata-kata yang telah kau ucapkan).**",
    "\ud83c\udf39 **Character": "Jun Naruse**",
    "\ud83c\udf41 **Anime": "Kokoro ga Sakebitagatterunda.**",
    "\ud83c\udf41 **Episode": "Episode 1**"
}
```

### 18. Qhacker

**Description**:
Dapatkan random Quotes Hacker

**Returns:**
  - **str**: Random Quotes Hacker

```python
from ApiNyaEr import apinya

result = await apinya.qhacker()
print(result)
```

#### Expected Output

```text
🃏 **Mereka menganggapku remeh dalam dunia nyata, tapi mereka tidak tahu aku di dalam 'Cyber World'.**
```

### 19. Qislam

**Description**:
Dapatkan random Quotes Islamic

**Returns:**
  - **str**: Random Quotes Islam

```python
from ApiNyaEr import apinya

result = await apinya.qislam()
print(result)
```

#### Expected Output

```text
📖 **Semoga memang dirimulah yang kelak menjadi pendamping hidupku**
```

### 20. Qpubg

**Description**:
Dapatkan random Quotes pubg

**Returns:**
  - **str**: Random Quotes Pubg

```python
from ApiNyaEr import apinya

result = await apinya.qpubg()
print(result)
```

#### Expected Output

```text
🏆 **Kami bukanlah player nob, kami hanya baru mulai**
```

### 21. Truth

**Description**:
Dapatkan Kata kata truth

**Returns:**
  - **str**: Random kata truth

```python
from ApiNyaEr import apinya

result = await apinya.truth()
print(result)
```

#### Expected Output

```text
Rahasia apa yg belum pernah kamu katakan sampai sekarang kepada teman mu ?
```

### 22. Wibu

**Description**:
Fetch spesifik Gambar/Gif Anime.

**Args:**
  - **endpoint (str)**: Kategori endpoin gambar/Gif animenya. Defaultnya
    "kiss".
    Valid Format endpoints:
    - "husbando", "kitsune", "neko", "waifu"
    Valid GIF endpoints:
    - "baka", "bite", "blush", "bored", "cry", "cuddle", "dance", "facepalm",
    "feed", "handhold", "handshake", "happy", "highfive", "hug", "kick",
    "kiss", "laugh", "lurk", "nod", "nom", "nope", "pat", "peck", "poke",
    "pout", "punch", "shoot", "shrug", "slap", "sleep", "smile", "smug",
    "stare", "think", "thumbsup", "tickle", "wave", "wink", "yawn", "yeet"
    amount (int): jumlah item gambarnya. Default 1.

**Returns:**
  - **dict**: Dictionary konten yang di request. Dictionarynya memiliki kata
    kunci`"results"`,
    yang menampung limit.

**Raises:**
  - **ValueError**: Jika endpoint tidak valid.

```python
from ApiNyaEr import apinya

result = await apinya.wibu(endpoint='kiss', amount=1)
print(result)
```

#### Expected Output

```json
{
    "results": [
        {
            "anime_name": "Hajimete no Gal",
            "url": "https://nekos.best/api/v2/kiss/16d3ee30-d62e-47ac-aa0b-3b7e81f2ac0b.gif"
        }
    ]
}
```


This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)