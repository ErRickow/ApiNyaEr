# ApiNyaEr
what

---

# 📘 API Documentation

Welcome to the **ErApi**! This library allows you to easily interact with the API using both **synchronous** and **asynchronous** options.

- **Sync**: `from ApiNyaEr.sync import apinya`
- **Async**: `from ApiNyaEr import apinya`

Below, we’ll cover each function, providing examples and expected results so you can get started quickly! Let’s dive in 🚀

## Status

| Function           | Status |
|--------------------|--------|
| [1. Ambil Doa](#1-ambil-doa) | ✅
| [2. Blackbox](#2-blackbox) | ❌
| [3. Carbon](#3-carbon) | ✅
| [4. Cat](#4-cat) | ✅
| [5. Cohere](#5-cohere) | ✅
| [6. Dare](#6-dare) | ✅
| [7. Dog](#7-dog) | ✅
| [8. Github Search](#8-github-search) | ✅
| [9. Hug](#9-hug) | ✅
| [10. Kapan Libur](#10-kapan-libur) | ✅
| [11. Password](#11-password) | ✅
| [12. Truth](#12-truth) | ✅


## 🎓 How to Use Each Function

### 1. Ambil Doa

**Description**:
Mengambil data doa dari API ItzPire berdasarkan nama doa.

**Args:**
  - **nama_doa (str)**: Nama doa yang ingin diambil.

**Returns:**
  - **str**: Teks doa yang diformat dengan rapi termasuk doa, ayat, latin, dan artinya.

```python
from ApiNyaEr import apinya

result = await apinya.ambil_doa(nama_doa='Tidur')
print(result)
```

#### Expected Output

```text
Doa sebelum tidur
Ayat: بِسْمِكَ االلّٰهُمَّ اَحْيَا وَبِاسْمِكَ اَمُوْتُ
Latin: Bismikallaahumma ahyaa wa ammuut
Artinya: Dengan menyebut nama Allah, aku hidup dan aku mati
```

### 2. Blackbox

**Description**:
Interact with the Blackbox AI API for generating content. 🧠

**Args:**
  - **args (str)**: The input text to interact with the Blackbox AI chat API.

**Returns:**
  - **requests.Response**: The response object from the API request.

```python
from ApiNyaEr import apinya

result = await apinya.blackbox(args='Tidur')
print(result)
```

#### Expected Output

```text
name 'urllib' is not defined
```

### 3. Carbon

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
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_o8oihSu1.png
```

### 4. Cat

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
https://cdn2.thecatapi.com/images/MTkyMjg3MQ.jpg
```

### 5. Cohere

**Description**:
Mengambil respons dari API AI ItzPire berdasarkan pertanyaan yang diberikan menggunakan metode POST.

**Args:**
  - **pertanyaan (str)**: Teks pertanyaan yang akan dikirim ke AI.

**Returns:**
  - **str**: Respons yang dihasilkan oleh AI.

```python
from ApiNyaEr import apinya

result = await apinya.cohere(pertanyaan='Tidur')
print(result)
```

#### Expected Output

```json
{
    "error": "Request failed with status code 429"
}
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
Minta tandatangan pada seorang guru yang paling kamu benci sambil bilang 'Anda benar-benar orang yang paling saya kagumi di dunia.'
```

### 7. Dog

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
https://random.dog/ba7d232f-e40c-40bb-a26b-3f0b5cd0e68a.jpg
```

### 8. Github Search

**Description**:
Pencarian GitHub untuk beberapa tipe konten.

**Args:**
  - **query (str)**: query Pencarian.
  - **search_type (str, optional)**: Type pencarian, terdiri dari:
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

result = await apinya.github_search(query='Tidur', search_type='repositories', max_results=3)
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

### 9. Hug

**Description**:
Dapatkan gif Random pelukan dari Nekos.Best API.

**Args:**
  - **amount (int)**: Jumlah gambar nya, Defaultnya 1.

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

### 10. Kapan Libur

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

### 11. Password

**Description**:
This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

**Description**:
Parameters: - num (int): The length of the generated password. Default is 12 if not specified.

**Returns:**
**Description**:
- str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.'

```python
from ApiNyaEr import apinya

result = await apinya.password(num=12)
print(result)
```

#### Expected Output

```text
&v^N$<8eJZ_T
```

### 12. Truth

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
Orang seperti apa yang ingin kamu nikahi suatu saat nanti?
```


This Project is Licensed under [MIT License](https://github.com/ErRickow/ApiNyaEr/blob/main/LICENSE)