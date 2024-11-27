

---

# 📘 API Documentation

Welcome to the **ErApi**! This library allows you to easily interact with the API using both **synchronous** and **asynchronous** options.

## Installation
To get started, make sure you have the library installed:
```bash
pip3 install ApiNyaEr
```

## Usage
- **Synchronous usage**: Import the library with:
```python
from ApiNyaEr.sync import apinya
```
- **Asynchronous usage**: Import the library with:
```python
from ApiNyaEr import apinya
```

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
| [11. Get Pinter Url](#11-get-pinter-url) | ❌
| [12. Github Search](#12-github-search) | ✅
| [13. Hug](#13-hug) | ✅
| [14. Kapan Libur](#14-kapan-libur) | ✅
| [15. Nama Epep](#15-nama-epep) | ✅
| [16. Password](#16-password) | ✅
| [17. Pypi](#17-pypi) | ❌
| [18. Qanime](#18-qanime) | ✅
| [19. Qhacker](#19-qhacker) | ✅
| [20. Qislam](#20-qislam) | ✅
| [21. Qpubg](#21-qpubg) | ✅
| [22. Truth](#22-truth) | ✅
| [23. Wibu](#23-wibu) | ✅


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
Kenapa awak tidur bilik saya.
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
https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/14044059/Kenali-Pola-Tidur-yang-Baik-untuk-Kesehatan.jpg.webp
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
    "results": "Generated by BLACKBOX.AI, try unlimited chat https://www.blackbox.ai\n\nTidur adalah proses fisiologis yang penting bagi kesehatan dan kesejahteraan manusia. Selama tidur, tubuh melakukan berbagai pemulihan dan regenerasi, termasuk pemulihan otot, penguatan sistem kekebalan tubuh, dan pengolahan informasi yang diperoleh selama hari. Tidur yang cukup dan berkualitas dapat meningkatkan konsentrasi, suasana hati, dan kesehatan secara keseluruhan.\n\nJika Anda memiliki pertanyaan lebih lanjut tentang tidur, seperti tips untuk tidur yang lebih baik atau dampak kurang tidur, silakan beri tahu!",
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
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_7lH7S3IE.png
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
https://cdn2.thecatapi.com/images/aat.jpg
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
Kirim sms pada tiga nomor acak di kontakmu dan tulis 'Aku baru saja menjadi model majalah Playboy.'
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
https://random.dog/0597fcdd-871c-487e-a62f-b3cab8937fda.mp4
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
🌾 **Telur segar tenggelam diair, telur yang kadaluarsa mengambang**
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
    "results": "**Definisi**\n\nTidur adalah keadaan istirahat alami di mana aktivitas fisik dan mental sangat berkurang. Tidur penting untuk kesehatan fisik, mental, dan emosional secara keseluruhan.\n\n**Jenis Tidur**\n\n* **Tidur NREM (Non-Rapid Eye Movement):** Fase tidur yang lebih dalam dan kurang aktif. Terdiri dari tiga tahap:\n    * Tidur Tahap 1: Tidur ringan dan transisi dari kesadaran ke tidur.\n    * Tidur Tahap 2: Tidur yang lebih dalam, aktivitas otak melambat.\n    * Tidur Tahap 3 (Tidur Gelombang Delta): Tidur terdalam, aktivitas otak sangat lambat.\n* **Tidur REM (Rapid Eye Movement):** Fase tidur aktif, ditandai dengan pergerakan mata yang cepat, mimpi yang jelas, dan aktivitas otak yang mirip dengan saat bangun.\n\n**Siklus Tidur**\n\nSiklus tidur normal terdiri dari serangkaian siklus NREM dan REM, berlangsung sekitar 90 menit. Biasanya kita mengalami 4-5 siklus tidur per malam.\n\n**Fungsi Tidur**\n\nTidur memainkan peran penting dalam berbagai fungsi, termasuk:\n\n* **Restorasi Fisik:** Memperbaiki jaringan, otot, dan hormon.\n* **Pemrosesan Kognitif:** Mengkonsolidasikan ingatan dan memproses informasi.\n* **Pengaturan Emosional:** Mendukung pengaturan suasana hati dan mengurangi stres.\n* **Fungsi Kekebalan Tubuh:** Meningkatkan sistem kekebalan tubuh.\n* **Kinerja Fisik:** Meningkatkan kekuatan, kecepatan, dan daya tahan.\n\n**Gangguan Tidur**\n\nAda berbagai gangguan tidur yang dapat memengaruhi kualitas tidur, antara lain:\n\n* Insomia\n* Apnea Tidur\n* Gangguan Irama Sirkadian\n* Gangguan Gerakan Periodik Tungkai\n* Narkolepsi\n\n**Kebutuhan Tidur**\n\nKebutuhan tidur bervariasi tergantung pada usia, individu, dan faktor lainnya. Rata-rata, sebagian besar orang dewasa membutuhkan 7-9 jam tidur per malam.\n\n**Cara Meningkatkan Kualitas Tidur**\n\nBeberapa tips untuk meningkatkan kualitas tidur meliputi:\n\n* Tetapkan jadwal tidur yang teratur.\n* Ciptakan lingkungan tidur yang nyaman (gelap, tenang, dingin).\n* Batasi konsumsi kafein dan alkohol sebelum tidur.\n* Lakukan aktivitas relaksasi sebelum tidur (yoga, membaca).\n* Hindari penggunaan perangkat elektronik sebelum tidur.\n* Jika sulit tidur, bangun dari tempat tidur dan lakukan aktivitas lain sampai mengantuk.\n* Konsultasikan dengan dokter jika masalah tidur berlanjut.",
    "author": "@chakszzz",
    "success": true
}
```

### 11. Get Pinter Url

**Description**:
Mengembalikan URL Pinterest berdasarkan query yang diberikan.

**Args:**
  - **query (str)**: Kata kunci pencarian untuk Pinterest.

**Returns:**
  - **str**: URL lengkap dengan query yang dimasukkan.

```python
from ApiNyaEr import apinya

result = await apinya.get_pinter_url(query='Tidur')
print(result)
```

#### Expected Output

```text
name 'self' is not defined
```

### 12. Github Search

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

### 13. Hug

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
        "anime_name": "Little Witch Academia",
        "url": "https://nekos.best/api/v2/hug/a3dfcc78-0c9b-4c74-ac1b-b259470a06e9.gif"
    }
]
```

### 14. Kapan Libur

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
Hari liburberikutnya adalah Hari Natal yang jatuh di hari Rabu, 25 Desember 2024 (28 hari lagi)
```

### 15. Nama Epep

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
【YWS】 Ꮓϵɾzxᴬᶜ 戈心
```

### 16. Password

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
KcGsr=`kdo(&
```

### 17. Pypi

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

### 18. Qanime

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
    "\ud83c\udf81 **Quotes": "Dia lebih mencemaskan temannya daripada dirinya sendiri. Dia lebih mementingkan temannya. Aku menghormati perasaannya. Jika kau ingin mencapai sesuatu, kau harus berusaha keras untuk mencapai semuanya.**",
    "\ud83c\udf39 **Character": "Subaru Natsuki**",
    "\ud83c\udf41 **Anime": "Re:Zero kara Hajimeru Isekai Seikatsu**",
    "\ud83c\udf41 **Episode": "Episode 9**"
}
```

### 19. Qhacker

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
🃏 **Hackers rarely have full knowledge of the technology stack of a target.**
```

### 20. Qislam

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
📖 **Jangan salahkan orang ketika kamu kecewa, tapi salahkan dirimu sendiri karena terlalu berharap sesuatu yang belum pasti**
```

### 21. Qpubg

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
🏆 **Aku tidak pernah menyukai chicken, tapi tidak dengan chicken di PUBG**
```

### 22. Truth

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
Kapan terakhir kali menangis dan mengapa?
```

### 23. Wibu

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
            "anime_name": "Date a Live",
            "url": "https://nekos.best/api/v2/kiss/ec4ea38c-2433-478b-83fd-897e7c750111.gif"
        }
    ]
}
```


This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)