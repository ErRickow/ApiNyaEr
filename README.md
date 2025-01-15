

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
| [2. Arti Nama](#2-arti-nama) | ✅
| [3. Bing Image](#3-bing-image) | ✅
| [4. Blackbox](#4-blackbox) | ✅
| [5. Carbon](#5-carbon) | ✅
| [6. Cat](#6-cat) | ✅
| [7. Dare](#7-dare) | ✅
| [8. Doa](#8-doa) | ✅
| [9. Dog](#9-dog) | ✅
| [10. Fakta Unik](#10-fakta-unik) | ✅
| [11. Fluxai](#11-fluxai) | ✅
| [12. Gemini](#12-gemini) | ✅
| [13. Get Pinter Url](#13-get-pinter-url) | ❌
| [14. Github Search](#14-github-search) | ✅
| [15. Hug](#15-hug) | ✅
| [16. Islam Ai](#16-islam-ai) | ✅
| [17. Kapan Libur](#17-kapan-libur) | ❌
| [18. Logo Maker](#18-logo-maker) | ❌
| [19. Luminai](#19-luminai) | ✅
| [20. Meta Ai](#20-meta-ai) | ✅
| [21. Nama Epep](#21-nama-epep) | ✅
| [22. Password](#22-password) | ✅
| [23. Pypi](#23-pypi) | ❌
| [24. Qanime](#24-qanime) | ✅
| [25. Qhacker](#25-qhacker) | ✅
| [26. Qislam](#26-qislam) | ✅
| [27. Qpubg](#27-qpubg) | ✅
| [28. Read Image](#28-read-image) | ✅
| [29. Terabox Dl](#29-terabox-dl) | ✅
| [30. Truth](#30-truth) | ✅
| [31. Wibu](#31-wibu) | ✅
| [32. Zodiak](#32-zodiak) | ✅


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
    "resultnya": "Tidur adalah proses penting bagi tubuh dan pikiran manusia. Selama tidur, tubuh melakukan berbagai pemulihan, seperti memperbaiki jaringan, memproses informasi, dan mengatur suasana hati. Tidur yang cukup dan berkualitas sangat diperlukan untuk menjaga kesehatan fisik dan mental. Jika ada yang ingin kamu ketahui lebih lanjut tentang tidur, seperti tips untuk tidur yang lebih baik atau dampak kurang tidur, silakan tanya!",
    "from": "ApiNyaEr",
    "join": "@Er_Support_Group"
}
```

### 2. Arti Nama

**Description**:
Mendapatkan arti nama dari string

**Args:**
  - **namanya (str)**: Nama Kamu
**Returns:**
  - **dict**: Informasi Arti Nama Kamu or Eror Msg

```python
from ApiNyaEr import apinya

result = await apinya.arti_nama(namanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "namanya": "Tidur",
    "artinya": "Peduli sesama, dermawan, tidak mementingkan diri sendiri, patuh terhadap kewajiban, ekspresi kreatif.\n\nAnda bukan tipe orang yang sombong. Anda menjadi bijaksana melalui berbagai macam pengalaman hidup yang sungguh-sungguh mengajarkan pelajaran untuk lebih mendekatkan diri kepada Tuhan dan berbuat baik bagi semua orang. Itu telah anda sadari betul, sehingga anda merasa tidak perlu untuk berbuat semena-mena atau menyombongkan diri. Anda orang yang sangat romantis dan dapat berkata-kata dengan indah. Anda juga menyukai bahasa dan kultur negara asing. Anda suka memberikan inspirasi kepada banyak orang. Sikap anda yang penuh dengan empati, keceriaan, dan penuh perhatian membuat anda manjadi tamu istimewa dalam setiap undangan. Anda orang yang cukup populer ditengah-tengah teman karena kebaikan yang mereka rasakan. Anda akan jauh lebih sukses apabila berkarir dalam hal-hal kemanusiaan, diplomat, translator, atau petinggi agama. Akan tetapi, apapun karir atau bisis yang anda pilih, itu semua akan berujung pada nilai-nilai kemanusiaan yang anda pegang tinggi karena sikap anda yang dermawan.",
    "from": "ApiNyaEr",
    "success": true
}
```

### 3. Bing Image

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

### 4. Blackbox

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

### 5. Carbon

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
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_Xt7fATmL.png
```

### 6. Cat

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
https://cdn2.thecatapi.com/images/e5r.jpg
```

### 7. Dare

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
Suruh bersiul pas mulutnya lagi penuh dijejelin makanan.
```

### 8. Doa

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

### 9. Dog

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
https://random.dog/e82e125b-94c4-4313-852d-6be6ae41da41.jpg
```

### 10. Fakta Unik

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
🌾 **Kuda Nil kentut lewat mulut.**
```

### 11. Fluxai

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

### 12. Gemini

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

### 13. Get Pinter Url

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

### 14. Github Search

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

### 15. Hug

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
        "anime_name": "Mononoke Hime",
        "url": "https://nekos.best/api/v2/hug/1e872929-e623-46ba-b5dc-fe05dfc61990.gif"
    }
]
```

### 16. Islam Ai

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
    "resultnya": "Maaf, saya tidak dapat memberikan informasi tentang tidur secara umum. Sebagai asisten yang berfokus pada Islam, saya hanya dapat memberikan penjelasan tentang tidur dari perspektif ajaran Islam. Berikut adalah beberapa ayat Al-Quran dan hadits terkait dengan tidur:\n\n\"Dan di antara tanda-tanda kekuasaan-Nya ialah tidurmu di waktu malam dan siang hari dan usahamu mencari sebagian dari karunia-Nya. Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda bagi kaum yang mendengarkan.\" (Quran 30:23)\n\n\"Dan Dialah yang menjadikan malam bagimu supaya kamu beristirahat padanya, dan (menjadikan) siang terang benderang (supaya kamu mencari karunia-Nya).\" (Quran 25:47)\n\nRasulullah SAW bersabda:\n\n\"Tidur adalah saudara kembar kematian.\" (HR. Ibnu Majah)\n\n\"Apabila salah seorang di antara kalian tidur, maka setan akan mengikatkan tiga simpul di atas kepalanya. Pada setiap simpul itu, setan akan mengucapkan, 'Bagimu malam yang panjang, maka tidurlah.' Apabila ia bangun dan mengingat Allah, maka satu simpul akan terlepas. Apabila ia berwudu, maka simpul yang lain akan terlepas. Dan apabila ia shalat, maka semua simpul itu akan terlepas, sehingga ia akan bangun di pagi hari dalam keadaan segar bugar.\" (HR. Bukhari)\n\nSaya sarankan untuk merujuk pada sumber-sumber Islam yang otoritatif untuk memahami lebih lanjut tentang tidur dari perspektif agama. Jika ada pertanyaan lain terkait Islam, saya akan berusaha menjawabnya dengan sebaik-baiknya.",
    "from": "ApiNyaEr",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 17. Kapan Libur

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

### 18. Logo Maker

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

### 19. Luminai

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
    "resultnya": "Tidur itu penting banget, bro! \ud83d\ude34 Bikin badan fresh dan siap buat ngegas lagi besok. Kalo lagi ngantuk, mending tidur aja deh. Jangan dipaksa, ya! \ud83d\ude04\u2728",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 20. Meta Ai

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
    "resultnya": "Tidur adalah kegiatan yang sangat penting bagi manusia. Tidur membantu kita untuk:\n\n\n## Fungsi Tidur\n\n1. Mengembalikan energi dan kekuatan tubuh\n2. Meningkatkan kesehatan mental dan emosional\n3. Membantu proses penyembuhan luka dan penyakit\n4. Meningkatkan konsentrasi dan produktivitas\n5. Mengatur hormon dan metabolisme tubuh\n\n\n## Manfaat Tidur yang Cukup\n\n1. Meningkatkan kualitas hidup\n2. Mengurangi risiko penyakit kronis (diabetes, hipertensi, jantung)\n3. Meningkatkan sistem imun\n4. Membantu mengatur berat badan\n5. Meningkatkan kesadaran dan kewaspadaan\n\n\n## Tips untuk Tidur yang Nyenyak\n\n1. Atur jam tidur secara teratur\n2. Buat suasana tidur nyaman (gelap, tenang, sejuk)\n3. Hindari kafein dan alkohol sebelum tidur\n4. Lakukan relaksasi (meditasi, yoga)\n5. Batasi penggunaan gadget sebelum tidur\n\n\nBerapa jam tidur yang Anda butuhkan setiap hari?",
    "from": "ApiNyaEr",
    "success": true
}
```

### 21. Nama Epep

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
꧁༺J꙰O꙰K꙰E꙰R꙰༻꧂
```

### 22. Password

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
3.0\U{1#]nJ-
```

### 23. Pypi

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

### 24. Qanime

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
    "\ud83c\udf81 **Quotes": "Saling menerima cinta satu sama lain adalah hal yang wajar. Jika dunia melarangnya, aku akan mengubah dunia ini meskipun harus menghancurkannya.**",
    "\ud83c\udf39 **Character": "Theo Cornaro**",
    "\ud83c\udf41 **Anime": "Grancrest Senki**",
    "\ud83c\udf41 **Episode": "Episode 20**"
}
```

### 25. Qhacker

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
🃏 **Saat berjudi, seseorang harus tahu lawan mereka, dan kelemahan mereka. Terutama, jika lawan itu adalah mesin.**
```

### 26. Qislam

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
📖 **Gak usah bingung seperti apa jodohmu kelak, Insyaallah dia tidak akan jauh daripada sifatmu saat ini**
```

### 27. Qpubg

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
🏆 **Kita tidak dilahirkan sebagai pemenang. Kita harus meraihnya sendiri dengan usaha dan kerja keras**
```

### 28. Read Image

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

### 29. Terabox Dl

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

### 30. Truth

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
Hal apa yang kamu rahasiakan sampe, sekarang dan gak ada satu orangpun yang tau?
```

### 31. Wibu

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
            "anime_name": "Sukitte Ii na yo",
            "url": "https://nekos.best/api/v2/kiss/ff5b70d7-f3c5-4c90-b10c-69c2ea1d90c5.gif"
        }
    ]
}
```

### 32. Zodiak

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
    "Why?": "Terjadi kesalahan: Request failed: 500, message='Internal Server Error', url='https://api.siputzx.my.id/api/primbon/zodiak?zodiak=Tidur'",
    "success": false,
    "report": "@Er_Support_Group"
}
```


This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)