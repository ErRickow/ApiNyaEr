

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
| [10. Fluxai](#10-fluxai) | ✅
| [11. Gemini](#11-gemini) | ✅
| [12. Get Pinter Url](#12-get-pinter-url) | ❌
| [13. Github Search](#13-github-search) | ✅
| [14. Hug](#14-hug) | ✅
| [15. Islam Ai](#15-islam-ai) | ✅
| [16. Kapan Libur](#16-kapan-libur) | ❌
| [17. Logo Maker](#17-logo-maker) | ❌
| [18. Luminai](#18-luminai) | ✅
| [19. Meta Ai](#19-meta-ai) | ✅
| [20. Nama Epep](#20-nama-epep) | ✅
| [21. Password](#21-password) | ✅
| [22. Pypi](#22-pypi) | ❌
| [23. Qanime](#23-qanime) | ✅
| [24. Qhacker](#24-qhacker) | ✅
| [25. Qislam](#25-qislam) | ✅
| [26. Qpubg](#26-qpubg) | ✅
| [27. Read Image](#27-read-image) | ✅
| [28. Terabox Dl](#28-terabox-dl) | ✅
| [29. Truth](#29-truth) | ✅
| [30. Wibu](#30-wibu) | ✅
| [31. Zodiak](#31-zodiak) | ✅


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

```json
{
    "resultnya": "Tidur adalah proses penting bagi tubuh dan pikiran manusia. Selama tidur, tubuh melakukan berbagai pemulihan, memperkuat sistem kekebalan, dan menyimpan memori. Tidur yang cukup dan berkualitas diperlukan untuk kesehatan fisik dan mental. \n\nBerbagai faktor dapat memengaruhi kualitas tidur, seperti stres, lingkungan, dan kebiasaan tidur. Penting untuk menciptakan rutinitas tidur yang baik, seperti menjadwalkan waktu tidur dan bangun yang konsisten, serta menciptakan lingkungan tidur yang nyaman.\n\nJika Anda memiliki pertanyaan lebih lanjut mengenai tidur atau tips untuk tidur yang lebih baik, silakan tanya!",
    "from": "ApiNyaEr",
    "join": "@Er_Support_Group"
}
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
https://t4.ftcdn.net/jpg/04/60/72/67/360_F_460726770_XFNB9Wx4VmXk2RRLBQDOz1gfy5kV5gBq.jpg
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
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_68ymGQtZ.png
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
https://cdn2.thecatapi.com/images/96j.jpg
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
Mecahin telur pake kepala.
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
https://random.dog/05f4b372-d8ff-42f0-8c11-b78c45d9eaa1.jpg
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
🌾 **Ada lebih dari 300 bakteri pembentuk karang gigi**
```

### 10. Fluxai

**Description**:
Generate image from Teks

**Returns:**
  - **input**: teks yang akan dijadikan image

```python
from ApiNyaEr import apinya

result = await apinya.fluxai(input='Tidur')
print(result)
```

#### Expected Output

```text
'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

### 11. Gemini

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

```text
None
```

### 12. Get Pinter Url

**Description**:
Mengembalikan hasil request Pinterest berdasarkan query yang diberikan.

**Args:**
  - **query (str)**: Kata kunci pencarian untuk Pinterest.

**Returns:**
  - **dict**: Respons JSON dari API Pinterest.

```python
from ApiNyaEr import apinya

result = await apinya.get_pinter_url(query='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 403, message='Forbidden', url='https://api.ryzendesu.vip/api/search/pinterest?query=Tidur'
```

### 13. Github Search

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
        "stargazers_count": 113,
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

### 14. Hug

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
        "anime_name": "Date a Live",
        "url": "https://nekos.best/api/v2/hug/a0fc88c6-a820-40b9-aa46-3ee273430ccc.gif"
    }
]
```

### 15. Islam Ai

**Description**:
args: tanya (str): teks pertanyaan

**Returns:**
    resultnya

```python
from ApiNyaEr import apinya

result = await apinya.islam_ai(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "resultnya": "Maaf, saya tidak dapat memberikan informasi tentang tidur secara umum. Sebagai asisten yang berfokus pada Islam, saya hanya dapat memberikan informasi yang berkaitan dengan pandangan Islam tentang tidur.\n\nDalam Islam, tidur dianggap sebagai salah satu tanda-tanda kekuasaan Allah SWT. Hal ini dijelaskan dalam Alquran:\n\n\"Dan di antara tanda-tanda kekuasaan-Nya ialah tidurmu di waktu malam dan siang hari dan usahamu mencari sebagian dari karunia-Nya. Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda bagi kaum yang mendengarkan.\" (Quran 30:23)\n\nRasulullah SAW juga bersabda:\n\n\"Tidur adalah saudara kembar kematian.\" (HR. Bukhari)\n\nDalam Islam, tidur dianggap sebagai salah satu bentuk ibadah dan istirahat bagi tubuh. Rasulullah SAW mengajarkan umatnya untuk tidur dengan niat yang baik dan mengucapkan doa sebelum tidur.\n\nJika Anda ingin informasi lebih lanjut tentang pandangan Islam mengenai tidur, saya sarankan untuk berkonsultasi dengan ulama atau sumber-sumber Islam yang terpercaya.",
    "from": "ApiNyaEr",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 16. Kapan Libur

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
'data'
```

### 17. Logo Maker

**Description**:
Membuat Logo Dari Input yang di masukkan

**Args:**
  - **input**: teks yang akan di buat Logo
**Returns:**
    resultnya else str(eror)

```python
from ApiNyaEr import apinya

result = await apinya.logo_maker(input='Tidur')
print(result)
```

#### Expected Output

```text
'method' object is not subscriptable
```

### 18. Luminai

**Args:**
  - **tanya (str)**: Teks query

**Returns:**
    resultnya

```python
from ApiNyaEr import apinya

result = await apinya.luminai(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "resultnya": "Wah, tidur itu penting banget, bro! \ud83d\ude34 Kalo udah ngantuk, mendingan langsung bobo aja. Nanti bangun-bangun, badan jadi segar lagi! Kapan terakhir kali kamu tidur nyenyak? \ud83c\udf19\u2728",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 19. Meta Ai

**Description**:
Bertanya pada meta AI

**Returns:**
  - **tanya(str)**: teks yang akan ditanyakan

```python
from ApiNyaEr import apinya

result = await apinya.meta_ai(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "resultnya": "Tidur adalah kegiatan yang sangat penting bagi manusia. Tidur membantu tubuh kita untuk beristirahat, memulihkan diri, dan mengembalikan energi. Selama tidur, tubuh kita melakukan beberapa proses penting seperti:\n\n\n## Proses Fisiologis\n\n1. **Pemulihan Otot**: Otot-otot yang lelah selama aktivitas sehari-hari diperbaiki dan dikembalikan ke kondisi normal.\n2. **Pengembalian Energi**: Tubuh mengisi kembali cadangan energi yang terkuras selama aktivitas.\n3. **Pembersihan Toksin**: Otak membersihkan diri dari toksin dan zat berbahaya yang menumpuk selama aktivitas.\n4. **Pengaturan Hormon**: Hormon-hormon seperti insulin, hormon pertumbuhan, dan hormon tiroid diatur dan diseimbangkan.\n\n\n## Manfaat Tidur\n\n1. **Meningkatkan Kesehatan Fisik**: Tidur yang cukup membantu mencegah penyakit kronis seperti diabetes, hipertensi, dan penyakit jantung.\n2. **Meningkatkan Kesehatan Mental**: Tidur yang cukup membantu mengurangi stres, kecemasan, dan depresi.\n3. **Meningkatkan Kinerja Otak**: Tidur yang cukup membantu meningkatkan konsentrasi, memori, dan kemampuan belajar.\n4. **Meningkatkan Kualitas Hidup**: Tidur yang cukup membantu meningkatkan kualitas hidup secara keseluruhan.\n\n\n## Tips untuk Tidur yang Nyenyak\n\n1. **Atur Waktu Tidur**: Pastikan waktu tidur yang konsisten setiap hari.\n2. **Ciptakan Lingkungan Nyaman**: Pastikan kamar tidur nyaman, gelap, dan sunyi.\n3. **Hindari Kafein dan Alkohol**: Hindari konsumsi kafein dan alkohol sebelum tidur.\n4. **Lakukan Relaksasi**: Lakukan aktivitas relaksasi seperti membaca buku atau mendengarkan musik sebelum tidur.\n\nBerapa jam tidur yang Anda butuhkan setiap hari?",
    "from": "ApiNyaEr",
    "success": true
}
```

### 20. Nama Epep

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
꧁༺༻꧂
```

### 21. Password

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
DHi6OQfxz[]3
```

### 22. Pypi

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

### 23. Qanime

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
    "\ud83c\udf81 **Quotes": "Cinta sejati adalah cinta yang tak dipengaruhi oleh penampilan. Jika penampilan orang bisa mempengaruhi perasaanmu, maka cintamu itu palsu.**",
    "\ud83c\udf39 **Character": "Chika Fujiwara**",
    "\ud83c\udf41 **Anime": "Kaguya-sama wa Kokurasetai?: Tensai-tachi no Renai Zunousen**",
    "\ud83c\udf41 **Episode": "Episode 5**"
}
```

### 24. Qhacker

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

### 25. Qislam

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
📖 **Terkadang bukan karena kita tahu caranya memuntahkan amarah tapi kita tahu jika makin marah tak akan menyelesaikan masalah**
```

### 26. Qpubg

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
🏆 **Skill individu boleh mumpuni. Tapi tanpa Kerja sama, tidak akan mencapai apa-apa**
```

### 27. Read Image

**Description**:
Bertanya gambar melalui url

**Returns:**
  - **url(str)**: string url

```python
from ApiNyaEr import apinya

result = await apinya.read_image(url='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 500, message='Internal Server Error', url='https://api.siputzx.my.id/api/ai/image2text?url=https://api.siputzx.my.id/api/ai/image2text'
```

### 28. Terabox Dl

**Args:**
  - **link (str)**: Teks query

**Returns:**
    resultnya

```python
from ApiNyaEr import apinya

result = await apinya.terabox_dl(link='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 500, message='Internal Server Error', url='https://vapis.my.id/api/terabox?url=Tidur'
```

### 29. Truth

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
Siapa di antara teman-temanmu yang menurutmu potongan rambutnya paling ngenes (paling nggak banget)?
```

### 30. Wibu

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
            "anime_name": "Infinite Stratos",
            "url": "https://nekos.best/api/v2/kiss/e6e811ae-c828-419b-a503-ef7a7bed228e.gif"
        }
    ]
}
```

### 31. Zodiak

**Description**:
Mengambil informasi zodiak berdasarkan input.

**Args:**
  - **input (str)**: Nama zodiak.

**Returns:**
  - **dict**: Informasi lengkap zodiak atau pesan kesalahan.

```python
from ApiNyaEr import apinya

result = await apinya.zodiak(input='Tidur')
print(result)
```

#### Expected Output

```json
{
    "message": "Terjadi kesalahan: Request failed: 500, message='Internal Server Error', url='https://api.siputzx.my.id/api/primbon/zodiak?zodiak=Tidur'",
    "success": false,
    "from": "ApiNyaEr"
}
```


This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)