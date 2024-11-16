# ApiNyaEr
what

---

# 📘 Dokumentasi ErApi

Selamat datang di **ErAI**! Perpustakaan ini memungkinkan Anda untuk berinteraksi dengan AI menggunakan opsi **sinkron** dan **asinkron**.

- **Sync**: `from ApiNyaEr.sync import apinya`
- **Async**: `from ApiNyaEr import apinya`

Berikut, kami akan membahas setiap fungsi, memberikan contoh dan hasil yang diharapkan agar Anda bisa mulai dengan cepat! Mari kita mulai 🚀

## Status

| Fungsi             | Status |
|--------------------|--------|
| [1. Ambil Doa](#1-ambil-doa) | ❌
| [2. Ambil Respons Ai](#2-ambil-respons-ai) | ✅
| [3. Carbon](#3-carbon) | ✅
| [4. Cat](#4-cat) | ❌
| [5. Dog](#5-dog) | ❌
| [6. Github Search](#6-github-search) | ✅
| [7. Hug](#7-hug) | ✅


## 🎓 Cara Menggunakan Setiap Fungsi

### 1. Ambil Doa

**Deskripsi**:
Mengambil data doa dari API ItzPire berdasarkan nama doa.

**Args:**
  - **nama_doa (str)**: Nama doa yang ingin diambil.

**Returns:**
  - **str**: Teks doa yang diformat dengan rapi termasuk doa, ayat, latin, dan artinya.

```python
from ApiNyaEr import apinya

result = await apinya.ambil_doa(nama_doa='Pokemon')
print(result)
```

#### Hasil yang Diharapkan

```text
Request failed: 500, message='Internal Server Error', url='https://itzpire.com/religion/islamic/doa?doaName=Pokemon'
```

### 2. Ambil Respons Ai

**Deskripsi**:
Mengambil respons dari API AI ItzPire berdasarkan pertanyaan yang diberikan.

**Args:**
  - **pertanyaan (str)**: Teks pertanyaan yang akan dikirim ke AI.

**Returns:**
  - **str**: Respons yang dihasilkan oleh AI.

```python
from ApiNyaEr import apinya

result = await apinya.ambil_respons_ai(pertanyaan='Pokemon')
print(result)
```

#### Hasil yang Diharapkan

```text
Tidak ada hasil
```

### 3. Carbon

**Deskripsi**:
Generates a code snippet image using the Carbon API, saves it to the downloads folder,
**Deskripsi**:
uploads it, and returns the URL of the uploaded image.

**Args:**
  - **query (str)**: The code snippet to be rendered as an image.

**Returns:**
  - **FilePath**: The file path of the saved image.

```python
from ApiNyaEr import apinya

result = await apinya.carbon(query='Pokemon')
print(result)
```

#### Hasil yang Diharapkan

```text
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_kPHtVgjk.png
```

### 4. Cat

**Deskripsi**:
Fetches a random cat image URL.

**Returns:**
  - **str or None**: The URL of a random cat image if available; None if no response is received.

```python
from ApiNyaEr import apinya

result = await apinya.cat()
print(result)
```

#### Hasil yang Diharapkan

```text
'cat'
```

### 5. Dog

**Deskripsi**:
Fetches a random dog image URL.

**Returns:**
  - **str or None**: The URL of a random dog image if available; None if no response is received.

```python
from ApiNyaEr import apinya

result = await apinya.dog()
print(result)
```

#### Hasil yang Diharapkan

```text
'dog'
```

### 6. Github Search

**Deskripsi**:
Searches GitHub for various types of content.

**Args:**
  - **query (str)**: The search query.
  - **search_type (str, optional)**: The type of search. Can be one of:
    - "repositories"
    - "users"
    - "organizations"
    - "issues"
    - "pull_requests"
    - "commits"
    - "topics"

**Deskripsi**:
Defaults to "repositories".
**Deskripsi**:
max_results (int, optional): The maximum number of results to return. Defaults to 3.

**Returns:**
  - **list**: A list of search results or an error message.

```python
from ApiNyaEr import apinya

result = await apinya.github_search(query='Pokemon', search_type='repositories', max_results=3)
print(result)
```

#### Hasil yang Diharapkan

```json
[
    {
        "name": "PokemonGo-Map",
        "full_name": "AHAAAAAAA/PokemonGo-Map",
        "description": "\ud83c\udf0f Live visualization of all the pokemon in your area... and more! (shutdown)",
        "url": "https://github.com/AHAAAAAAA/PokemonGo-Map",
        "language": null,
        "stargazers_count": 7529,
        "forks_count": 2815
    },
    {
        "name": "pokemon-showdown",
        "full_name": "smogon/pokemon-showdown",
        "description": "Pok\u00e9mon battle simulator.",
        "url": "https://github.com/smogon/pokemon-showdown",
        "language": "TypeScript",
        "stargazers_count": 4796,
        "forks_count": 2799
    },
    {
        "name": "PokemonGo-Bot",
        "full_name": "PokemonGoF/PokemonGo-Bot",
        "description": "The Pokemon Go Bot, baking with community.",
        "url": "https://github.com/PokemonGoF/PokemonGo-Bot",
        "language": "Python",
        "stargazers_count": 3871,
        "forks_count": 1543
    }
]
```

### 7. Hug

**Deskripsi**:
Fetches a specified number hug gif from the Nekos.Best API.

**Args:**
  - **amount (int)**: The number of neko images to fetch. Defaults to 1.

**Returns:**
  - **list**: A list of dictionaries containing information about each fetched neko image or GIF.
    Each dictionary typically includes:
    - anime_name (str): The name of the anime.
    - url (str): The URL of the GIF.

```python
from ApiNyaEr import apinya

result = await apinya.hug(amount=1)
print(result)
```

#### Hasil yang Diharapkan

```json
[
    {
        "anime_name": "Inu x Boku Secret Service",
        "url": "https://nekos.best/api/v2/hug/e868c5a9-a440-491a-a96b-fda4953202f7.gif"
    }
]
```


Proyek ini dilisensikan di bawah [MIT License](https://github.com/ErRickow/ApiNyaEr/blob/main/LICENSE)