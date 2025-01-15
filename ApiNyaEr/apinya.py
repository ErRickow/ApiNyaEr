import json
import os
import random
import re
import string
import urllib
from base64 import b64decode as apainier
from os.path import realpath
from typing import Union

import aiofiles
import aiohttp
import requests

from .fungsi import FilePath
from .td import DARE, TRUTH
from .teks import ANIMEK, EPEP, FAKTA, HECKER, ISLAMIC, PUBG


class ErApi:
    def __init__(self):
        self.base_urls = {
            "siputx": apainier("aHR0cHM6Ly9hcGkuc2lwdXR6eC5teS5pZC9hcGk=").decode(
                "utf-8"
            ),
            "flux": apainier(
                "aHR0cHM6Ly9hcGkuc2lwdXR6eC5teS5pZC9hcGkvYWkvZmx1eA=="
            ).decode("utf-8"),
            "ai": apainier("aHR0cHM6Ly92YXBpcy5teS5pZC9hcGkvb3BlbmFp").decode("utf-8"),
            "hehe": apainier("aHR0cHM6Ly92YXBpcy5teS5pZC9hcGkvbG9nb21ha2Vy").decode(
                "utf-8"
            ),
            "whe": apainier("aHR0cHM6Ly92YXBpcy5teS5pZC9hcGkvaXNsYW1haQ==").decode(
                "utf-8"
            ),
            "njir": apainier("aHR0cHM6Ly92YXBpcy5teS5pZC9hcGkvdGVyYWJveA==").decode(
                "utf-8"
            ),
            "luminai": apainier(
                "aHR0cHM6Ly9yZXN0LWVyLWFwaS52ZXJjZWwuYXBwL2x1bWluYWk="
            ).decode("utf-8"),
            "pinter": "https://api.ryzendesu.vip/api/search/pinterest?query={query}",
            "neko_url": apainier(
                "aHR0cHM6Ly9uZWtvcy5iZXN0L2FwaS92Mi97ZW5kcG9pbnR9P2Ftb3VudD17YW1vdW50fQ=="
            ).decode("utf-8"),
            "neko_hug": apainier(
                "aHR0cHM6Ly9uZWtvcy5iZXN0L2FwaS92Mi9odWc/YW1vdW50PXt9"
            ).decode("utf-8"),
            "doa_url": apainier(
                "aHR0cHM6Ly9pdHpwaXJlLmNvbS9yZWxpZ2lvbi9pc2xhbWljL2RvYQ=="
            ).decode("utf-8"),
            "cat": apainier(
                "aHR0cHM6Ly9hcGkudGhlY2F0YXBpLmNvbS92MS9pbWFnZXMvc2VhcmNo"
            ).decode("utf-8"),
            "dog": apainier("aHR0cHM6Ly9yYW5kb20uZG9nL3dvb2YuanNvbg==").decode("utf-8"),
            "randy": "https://private-akeno.randydev.my.id/ryuzaki/chatgpt-old",
            "libur": apainier(
                "aHR0cHM6Ly9pdHpwaXJlLmNvbS9pbmZvcm1hdGlvbi9uZXh0TGlidXI="
            ).decode("utf-8"),
            "bing_image": apainier(
                "aHR0cHM6Ly93d3cuYmluZy5jb20vaW1hZ2VzL2FzeW5j"
            ).decode("utf-8"),
            "pypi": apainier("aHR0cHM6Ly9weXBpLm9yZy9weXBp").decode("utf-8"),
        }

    async def _make_request(
        self,
        url: str,
        method: str = "GET",
        params: dict = None,
        data: dict = None,
        files: dict = None,
        headers: dict = None,
        verify: bool = True,
    ) -> Union[dict, str]:
        """
        Membuat permintaan HTTP asinkron ke URL yang ditentukan dengan parameter, header, dan data opsional.

        Args:
            url (str): URL tujuan permintaan dikirimkan.
            method (str, opsional): Metode HTTP yang digunakan (misalnya, "GET", "POST"). Default: "GET".
            params (dict, opsional): Parameter kueri yang disertakan dalam permintaan. Default: None.
            data (dict, opsional): Data yang disertakan dalam body permintaan (untuk permintaan POST). Default: None.
            files (dict, opsional): File yang diunggah dalam permintaan (jika ada). Default: None.
            headers (dict, opsional): Header yang disertakan dalam permintaan. Default: None.
            verify (bool, opsional): Apakah sertifikat SSL harus diverifikasi. Default: True.

        Returns:
            Union[dict, str]: Respons JSON dalam bentuk dictionary jika respons diformat sebagai JSON,
                              jika tidak, mengembalikan respons sebagai string.

        Result:
            ValueError: Jika permintaan gagal karena kesalahan klien.
        """
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                    headers=headers,
                    ssl=verify,
                ) as response:
                    response.raise_for_status()
                    if "application/json" in response.headers.get("Content-Type", ""):
                        return await response.json()
                    return await response.text()
            except aiohttp.ClientError as e:
                raise ValueError(f"Request failed: {str(e)}")

    async def get_pinter_url(self, query: str) -> dict:
        """
        Mengembalikan hasil request Pinterest berdasarkan query yang diberikan.

        Args:
            query (str): Kata kunci pencarian untuk Pinterest.

        Returns:
            dict: Respons JSON dari API Pinterest.
        """
        url = self.base_urls["pinter"].format(query=query)
        anunya = await self._make_request(url)
        return anunya if anunya else None

    async def wibu(self, endpoint: str = "kiss", amount: int = 1) -> dict:
        """Fetch spesifik Gambar/Gif Anime.

        Args:
            endpoint (str): Kategori endpoin gambar/Gif animenya. Defaultnya
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

        Returns:
            dict: Dictionary konten yang di request. Dictionarynya memiliki kata
            kunci`"results"`,
                  yang menampung limit.

        Raises:
            ValueError: Jika endpoint tidak valid.
        """
        valid_categories = [
            "husbando",
            "kitsune",
            "neko",
            "waifu",  # Images
            "baka",
            "bite",
            "blush",
            "bored",
            "cry",
            "cuddle",
            "dance",
            "facepalm",
            "feed",
            "handhold",
            "handshake",
            "happy",
            "highfive",
            "hug",
            "kick",
            "kiss",
            "laugh",
            "lurk",
            "nod",
            "nom",
            "nope",
            "pat",
            "peck",
            "poke",
            "pout",
            "punch",
            "shoot",
            "shrug",
            "slap",
            "sleep",
            "smile",
            "smug",
            "stare",
            "think",
            "thumbsup",
            "tickle",
            "wave",
            "wink",
            "yawn",
            "yeet",  # GIFs
        ]

        if endpoint not in valid_categories:
            raise ValueError(
                f"SALAH GUOBLOK'{endpoint}'. Harus yang kek gini: {', '.join(valid_categories)}"
            )

        url = self.base_urls["neko_url"].format(endpoint=endpoint, amount=amount)

        response = await self._make_request(url)

        return response

    @staticmethod
    def password(num: int = 12) -> str:
        """
        Fungsi ini menghasilkan kata sandi acak dengan menggabungkan huruf besar, huruf kecil, tanda baca, dan digit.

        Parameters:
        - num (int): Panjang kata sandi yang dihasilkan. Default adalah 12 jika tidak ditentukan.

        Returns:
        - str: Kata sandi yang dihasilkan secara acak yang terdiri dari karakter dari string.ascii_letters, string.punctuation, dan string.digits.
        """
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(random.sample(characters, num))
        return password

    def _rnd_str(self):
        """
        Generates a random string of 8 alphanumeric characters.

        Returns:
            str: A random 8-character alphanumeric string.
        """
        random_str = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        return random_str

    @staticmethod
    def gemini(tanya: str) -> dict:
        """
        Berinteraksi dengan Gemini AI. ✨

        Args:
            tanya (str): Teks yang di berikan.

        Returns:
            dict: dictionaries yang berisi konten ai nya.
        """
        url = apainier(
            "aHR0cHM6Ly9nZW5lcmF0aXZlbGFuZ3VhZ2UuZ29vZ2xlYXBpcy5jb20vdjFiZXRhL21vZGVscy9nZW1pbmktcHJvOmdlbmVyYXRlQ29udGVudD9rZXk9QUl6YVN5QmtOSlVub3BEaEFvVmU3dVJqZ0gzeElPSnZBdHJ6Zk9J"
        ).decode("utf-8")
        headers = {"Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": tanya}]}]}

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                generated_text = response.json()["candidates"][0]["content"]["parts"][
                    0
                ]["text"]
                return {
                    "results": generated_text,
                    "author": "@chakszzz",
                    "success": True,
                }
        except Exception as e:
            return e

    @staticmethod
    def truth():
        """
        Dapatkan Kata kata truth

        Returns:
            str: Random kata truth
        """
        truthnya = random.choice(TRUTH)
        return truthnya

    @staticmethod
    def qanime():
        """
        Dapatkan Kata kata anime

        Returns:
            str: Random kata anime
        """
        mmk = random.choice(ANIMEK)
        return mmk

    @staticmethod
    def dare():
        """
        Dapatkan Kata kata dare

        Returns:
            str: Random kata dare
        """
        darenya = random.choice(DARE)
        return darenya

    @staticmethod
    def nama_epep():
        """
        Dapatkan random nama ep ep

        Returns:
            str: Random nama ep epnya
        """
        namanya = random.choice(EPEP)
        return namanya

    @staticmethod
    def qpubg():
        """
        Dapatkan random Quotes pubg

        Returns:
            str: Random Quotes Pubg
        """
        kntlny = random.choice(PUBG)
        return kntlny

    @staticmethod
    def qhacker():
        """
        Dapatkan random Quotes Hacker

        Returns:
            str: Random Quotes Hacker
        """
        mmk = random.choice(HECKER)
        return mmk

    @staticmethod
    def qislam():
        """
        Dapatkan random Quotes Islamic

        Returns:
            str: Random Quotes Islam
        """
        Sabyan = random.choice(ISLAMIC)
        return Sabyan

    @staticmethod
    def fakta_unik():
        """
        Dapatkan random Seputar Fakta Unik

        Returns:
            str: Random Fakta
        """
        kntlny = random.choice(FAKTA)
        return kntlny

    @staticmethod
    def blackbox(tanya: str) -> requests.Response:
        """
        Berinteraksi dengan Blackbox AI untuk menghasilkan konten. 🧠

        Args:
            tanya (str): Teks masukan untuk berinteraksi dengan API obrolan Blackbox AI.

        Returns:
            requests.Response: Objek respons dari permintaan API.
        """

        url = apainier("aHR0cHM6Ly9hcGkuYmxhY2tib3guYWkvYXBpL2NoYXQ=").decode("utf-8")

        payload = {
            "agentMode": {},
            "codeModelMode": True,
            "id": "XM7KpOE",
            "isMicMode": False,
            "maxTokens": None,
            "messages": [
                {
                    "id": "XM7KpOE",
                    "content": urllib.parse.unquote(tanya),
                    "role": "user",
                }
            ],
            "previewToken": None,
            "trendingAgentMode": {},
            "userId": "87cdaa48-cdad-4dda-bef5-6087d6fc72f6",
            "userSystemPrompt": None,
        }

        headers = {
            "Content-Type": "application/json",
            "Cookie": "sessionId=f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf; intercom-id-jlmqxicb=4cf07dd8-742e-4e3f-81de-38669816d300; intercom-device-id-jlmqxicb=1eafaacb-f18d-402a-8255-b763cf390df6; intercom-session-jlmqxicb=",
            "Origin": apainier("aHR0cHM6Ly9hcGkuYmxhY2tib3guYWk=").decode("utf-8"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return {
                    "results": response.text.strip(),
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as e:
            return e

    async def arti_nama(self, namanya: str):
        """
        Mendapatkan arti nama dari string

        Args:
            namanya (str): Nama Kamu
        Returns:
            dict: Informasi Arti Nama Kamu or Eror Msg
        """
        url = f"{self.base_urls['siputx']}/primbon/artinama"
        par = {"nama": namanya}
        try:
            res = await self._make_request(url, params=par)
            if res["status"] is True:
                return {
                    "namanya": res["data"]["nama"],
                    "artinya": res["data"]["arti"],
                    "from": "ApiNyaEr",
                    "success": True,
                }
            else:
                return {
                    "Why?": "gagal mendapatkan arti nama.",
                    "success": False,
                    "report": "@Er_Support_Group",
                }
        except Exception as r:
            return {
                "Why?": f"Terjadi kesalahan: {str(r)}",
                "success": False,
                "report": "@Er_Support_Group",
            }

    async def zodiak(self, input: str):
        """
        Mengambil informasi zodiak berdasarkan input.

        Args:
            input (str): Nama zodiak.

        Returns:
            dict: Informasi lengkap zodiak atau pesan kesalahan.
        """
        url = f"{self.base_urls['siputx']}/primbon/zodiak"
        par = {"zodiak": input}
        try:
            res = await self._make_request(url, params=par)
            if res["status"] is True:
                data = res["data"]
                return {
                    "zodiak": data["zodiak"],
                    "nomor_keberuntungan": data["nomor_keberuntungan"],
                    "aroma_keberuntungan": data["aroma_keberuntungan"],
                    "planet_yang_mengitari": data["planet_yang_mengitari"],
                    "bunga_keberuntungan": data["bunga_keberuntungan"],
                    "warna_keberuntungan": data["warna_keberuntungan"],
                    "batu_keberuntungan": data["batu_keberuntungan"],
                    "elemen_keberuntungan": data["elemen_keberuntungan"],
                    "pasangan_zodiak": data["pasangan_zodiak"],
                    "success": True,
                    "from": "ApiNyaEr",
                }
            else:
                return {
                    "Why?": "Gagal mendapatkan data zodiak.",
                    "success": False,
                    "report": "@Er_Support_Group",
                }
        except Exception as r:
            return {
                "Why?": f"Terjadi kesalahan: {str(r)}",
                "success": False,
                "report": "@Er_Support_Group",
            }

    async def read_image(self, urlnya: str):
        """
        Bertanya gambar melalui url

        Returns:
            url(str): string url
        """
        url = f"{self.base_urls['siputx']}/ai/image2text"
        urlnya = "https://cataas.com/cat"
        par = {"url": urlnya}
        try:
            res = await self._make_request(url, params=par)
            if res["status"] is True:
                return {
                    "resultnya": res["data"],
                    "from": "ApiNyaEr",
                    "success": True,
                }
        except Exception as r:
            return str(r)

    async def meta_ai(self, tanya: str):
        """
        Bertanya pada meta AI

        Returns:
            tanya(str): teks yang akan ditanyakan
        """
        url = f"{self.base_urls['siputx']}/ai/metaai"
        par = {"query": tanya}
        try:
            res = await self._make_request(url, params=par)
            if res["status"] is True:
                return {
                    "resultnya": res["data"],
                    "from": "ApiNyaEr",
                    "success": True,
                }
        except Exception as r:
            return str(r)

    async def fluxai(self, input: str):
        """
        Generate image from Teks

        Returns:
            input: teks yang akan dijadikan image
        """
        params = {"prompt": input}
        try:
            res = await self._make_request(self.base_urls["flux"], params=params)
            return res
        except Exception as r:
            return str(r)

    async def kapan_libur(self):
        """
        Dapatkan informasi Hari libur kedepan.

        Returns:
            str: Hari Libur Berikutnya.
        """
        response = requests.get(self.base_urls["libur"]).json()
        next_libur = response["data"]["nextLibur"]
        return next_libur

    async def terabox_dl(self, link: str):
        """
        Args:
            link (str): Teks query

        Returns:
            resultnya
        """
        params = {"url": link}
        try:
            response = await self._make_request(self.base_urls["njir"], params=params)
            if response["data"]:
                return {
                    "judul": response["data"]["filename"],
                    "ukuran": response["data"]["size"],
                    "url": response["data"]["download"],
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as e:
            return e

    async def islam_ai(self, tanya: str):
        """
        args:
            tanya (str): teks pertanyaan

        Returns:
            resultnya
        """
        paman = {"q": tanya}
        try:
            res = await self._make_request(self.base_urls["whe"], params=paman)
            if res["status"] == True:
                return {
                    "resultnya": res["result"],
                    "from": "ApiNyaEr",
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as r:
            return str(r)

    async def logo_maker(self, input: str):
        """
        Membuat Logo Dari Input yang di masukkan

        Args:
            input: teks yang akan di buat Logo
        Returns:
            resultnya else str(eror)
        """
        url = self._make_request["hehe"]
        parang = {"q": input}
        try:
            res = await self._make_request(url, params=parang)
            return res
        except Exception as r:
            return r

    async def luminai(self, tanya: str):
        """
        Args:
            tanya (str): Teks query

        Returns:
            resultnya
        """
        params = {"text": tanya}
        try:
            response = await self._make_request(
                self.base_urls["luminai"], params=params
            )
            if response["data"]:
                return {
                    "resultnya": response["data"]["result"],
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as e:
            return e

    async def ai(self, tanya: str):
        """
        Interaksi dengan AI Basis Text.

        Args:
        tanya (str): Text inputnya.

        Returns:
        str: Respon chatbotnya.
        """
        url = self.base_urls["ai"]
        par = {"q": tanya}
        try:
            res = await self._make_request(url, params=par)
            if res["status"] == True:
                return {
                    "resultnya": res["result"],
                    "from": "ApiNyaEr",
                    "join": "@Er_Support_Group",
                }
        except Exception as er:
            return er

    async def doa(self, nama_doa: str) -> str:
        """
        Mengambil data doa dari API ItzPire berdasarkan nama doa.

        Args:
            nama_doa (str): Nama doa yang ingin diambil.

        Returns:
            str: Teks doa yang diformat dengan rapi termasuk doa, ayat, latin, dan artinya.
        """
        url = self.base_urls["doa_url"]
        params = {"doaName": nama_doa}
        respons = await self._make_request(url, params=params)

        if (
            isinstance(respons, dict)
            and respons.get("status") == "success"
            and "data" in respons
        ):
            data_doa = respons["data"]
            return (
                f"{data_doa.get('doa', 'Tidak tersedia')}\n"
                f"Ayat: {data_doa.get('ayat', 'Tidak tersedia')}\n"
                f"Latin: {data_doa.get('latin', 'Tidak tersedia')}\n"
                f"Artinya: {data_doa.get('artinya', 'Tidak tersedia')}"
            )
        return "Doa tidak ditemukan atau format data tidak valid."

    async def bing_image(self, teks: str, limit: int = 1):
        """
        Cari bing images based om teks.

        Args:
            teks (str): Teks quesy yang ingin di cari gambarnya.
            limit (int, optional): Maximum number photonya. Defaults nya 1.

        Returns:
            list: List image url yang di terima.
        """
        data = {
            "q": teks,
            "first": 0,
            "count": limit,
            "adlt": "off",
            "qft": "",
        }
        response = await self._make_request(self.base_urls["bing_image"], params=data)
        return re.findall(r"murl&quot;:&quot;(.*?)&quot;", response) if response else []

    async def carbon(self, query):
        """
        Args:
            query (str): Potongan kode yang akan dirender sebagai gambar.

        Return:
            FilePath: Jalur file dari gambar yang disimpan.
        """
        async with aiohttp.ClientSession(
            headers={"Content-Type": "application/json"},
        ) as ses:
            params = {
                "code": query,
            }
            try:
                response = await ses.post(
                    "https://carbonara.solopov.dev/api/cook",
                    json=params,
                )
                response_data = await response.read()
            except aiohttp.client_exceptions.ClientConnectorError:
                raise ValueError("Can not reach the Host!")

            downloads_folder = "downloads"
            os.makedirs(downloads_folder, exist_ok=True)

            file_path = os.path.join(downloads_folder, f"carbon_{self._rnd_str()}.png")

            async with aiofiles.open(file_path, "wb") as f:
                await f.write(response_data)

            return FilePath(realpath(file_path))

    async def github_search(self, cari, tipe="repositories", max_results=3):
        """
        Pencarian GitHub untuk beberapa tipe konten.

        Args:
            cari (str): untuk Pencarian.
            tipe (str, optional): Type pencarian, terdiri dari:
                - "repositories"
                - "users"
                - "organizations"
                - "issues"
                - "pull_requests"
                - "commits"
                - "topics"

                Defaults ke "repositories".
            max_results (int, optional): Maximum nomor dari results untuk
            return. Defaultnya 3.

        Returns:
            list: List dari pencarian results atau pesan error.
        """
        tipe_yang_valid = [
            "repositories",
            "users",
            "organizations",
            "issues",
            "pull_requests",
            "commits",
            "topics",
        ]

        if tipe not in tipe_yang_valid:
            return {
                "error": f"Type pencarian salah guoblok. Tipe validnya kek gini: {tipe_yang_valid}"
            }

        url_mapping = {
            "pull_requests": "https://api.github.com/search/issues",
            "organizations": "https://api.github.com/search/users",
            "topics": "https://api.github.com/search/topics",
        }

        if tipe in url_mapping:
            url = url_mapping[tipe]
            if tipe == "pull_requests":
                cari += " type:pr"
            elif tipe == "organizations":
                cari += " type:org"
        else:
            url = f"https://api.github.com/search/{tipe}"

        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": cari, "per_page": max_results}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            items = results.get("items", [])

            result_list = []

            for item in items:
                item_info = {}
                if tipe == "repositories":
                    item_info = {
                        "name": item["name"],
                        "full_name": item["full_name"],
                        "description": item["description"],
                        "url": item["html_url"],
                        "language": item.get("language"),
                        "stargazers_count": item.get("stargazers_count"),
                        "forks_count": item.get("forks_count"),
                    }
                elif tipe in ["users", "organizations"]:
                    item_info = {
                        "login": item["login"],
                        "id": item["id"],
                        "url": item["html_url"],
                        "avatar_url": item.get("avatar_url"),
                        "type": item.get("type"),
                        "site_admin": item.get("site_admin"),
                        "name": item.get("name"),
                        "company": item.get("company"),
                        "blog": item.get("blog"),
                        "location": item.get("location"),
                        "email": item.get("email"),
                        "bio": item.get("bio"),
                        "public_repos": item.get("public_repos"),
                        "public_gists": item.get("public_gists"),
                        "followers": item.get("followers"),
                        "following": item.get("following"),
                    }
                elif tipe in ["issues", "pull_requests"]:
                    item_info = {
                        "title": item["title"],
                        "user": item["user"]["login"],
                        "state": item["state"],
                        "url": item["html_url"],
                        "comments": item.get("comments"),
                        "created_at": item.get("created_at"),
                        "updated_at": item.get("updated_at"),
                        "closed_at": item.get("closed_at"),
                    }
                elif tipe == "commits":
                    item_info = {
                        "sha": item["sha"],
                        "commit_message": item["commit"]["message"],
                        "author": item["commit"]["author"]["name"],
                        "date": item["commit"]["author"]["date"],
                        "url": item["html_url"],
                    }
                elif tipe == "topics":
                    item_info = {
                        "name": item["name"],
                        "display_name": item.get("display_name"),
                        "short_description": item.get("short_description"),
                        "description": item.get("description"),
                        "created_by": item.get("created_by"),
                        "url": item.get("url") if "url" in item else None,
                    }

                result_list.append(item_info)

            return result_list

        except requests.exceptions.RequestException as e:
            return {"error": f"Requestnya Error: {e}"}
        except requests.exceptions.HTTPError as e:
            return {
                "error": f"HTTP error: {e.response.status_code} - {e.response.text}"
            }
        except KeyError as e:
            return {"error": f"Key error: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

    async def cat(self):
        """
        Generate random gambar kucing.

        Returns:
            str or None: Url random kucing ataupun None; None jika response
            tidak di terima.
        """
        response = await self._make_request(self.base_urls["cat"])
        return response[0]["url"] if response else None

    async def dog(self):
        """
        Dapatkan random foto anjing.

        Returns:
            str or None: Url Random anjing jika tersedia; None jika tidak ada
            response yang di terima.
        """
        response = await self._make_request(self.base_urls["dog"])
        return response["url"] if response else None

    async def hug(self, amount: int = 1) -> list:
        """Dapatkan gif Random pelukan dari Nekos.Best API.

        Args:
            amount (int): amount gambar nya, Defaultnya 1.

        Returns:
            list: List dari dictionaries tentang informasi neko image atau GIF.
                  Type dictionaries:
                  - anime_name (str): Nama anime.
                  - url (str): Url gif nya.
        """
        response = await self._make_request(self.base_urls["neko_hug"].format(amount))
        return response["results"]

    async def pypi(self, namanya):
        """
        Mengambil informasi metadata tentang paket Python tertentu dari API PyPI.

        Args:
            namanya (str): Nama paket yang dicari di PyPI.

        Returns:
            dict atau None: Sebuah kamus dengan informasi relevan tentang paket jika ditemukan, yang berisi:
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
         Returns None jika paket tidak ditemukan atau terjadi kesalahan.
        """
        url = f"{self.base_urls['pypi']}/{namanya}/json"
        response = await self._make_request(url)
        if response:
            info = response["info"]
            relevant_info = {
                "name": info["name"],
                "version": info["version"],
                "summary": info["summary"],
                "author": info["author"],
                "author_email": info["author_email"],
                "license": info["license"],
                "home_page": info["home_page"],
                "package_url": info["package_url"],
                "requires_python": info["requires_python"],
                "keywords": info["keywords"],
                "classifiers": info["classifiers"],
                "project_urls": info["project_urls"],
            }
            return relevant_info
        else:
            return "TOLOL"


apinya = ErApi()
