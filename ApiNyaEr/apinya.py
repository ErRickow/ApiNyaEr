import os
import random
import string
from os.path import realpath
from typing import Union
from base64 import b64decode as apainier
from urllib

import aiofiles
import aiohttp
import requests

from .fungsi import FilePath
from .td import TRUTH, DARE

class ErApi:
    def __init__(self):
        self.base_urls = {
            "neko_url": "https://nekos.best/api/v2/{endpoint}?amount={amount}",
            "neko_hug": "https://nekos.best/api/v2/hug?amount={}",
            "doa_url": "https://itzpire.com/religion/islamic/doa",
            "ai_url": "https://itzpire.com/ai/cohere",
            "cat": "https://api.thecatapi.com/v1/images/search",
            "dog": "https://random.dog/woof.json",
            "randy": "https://private-akeno.randydev.my.id/ryuzaki/chatgpt-old",
            "libur": "https://itzpire.com/information/nextLibur",
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

    @staticmethod
    def password(num: int = 12) -> str:
        """
        This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

        Parameters:
        - num (int): The length of the generated password. Default is 12 if not specified.

        Returns:
        - str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.'
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
    def truth():
        """
        Dapatkan Kata kata truth
        
        Returns:
            str: Random kata truth
        """
        truthnya=random.choice(TRUTH)
        return truthnya

    @staticmethod
    def dare():
        """
        Dapatkan Kata kata dare
        
        Returns:
            str: Random kata dare
        """
        darenya=random.choice(DARE)
        return darenya

    @staticmethod
    def blackbox(args: str) -> requests.Response:
        """
        Interact with the Blackbox AI API for generating content. 🧠

        Args:
            args (str): The input text to interact with the Blackbox AI chat API.

        Returns:
            requests.Response: The response object from the API request.
        """

        url = apainier('aHR0cHM6Ly93d3cuYmxhY2tib3guYWkvYXBpL2NoYXQ=').decode("utf-8")
        
        payload = {
            "agentMode": {},
            "codeModelMode": True,
            "id": "XM7KpOE",
            "isMicMode": False,
            "maxTokens": None,
            "messages": [
                {
                    "id": "XM7KpOE",
                    "content": urllib.parse.unquote(args),
                    "role": "user"
                }
            ],
            "previewToken": None,
            "trendingAgentMode": {},
            "userId": "87cdaa48-cdad-4dda-bef5-6087d6fc72f6",
            "userSystemPrompt": None
        }

        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'sessionId=f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf; intercom-id-jlmqxicb=4cf07dd8-742e-4e3f-81de-38669816d300; intercom-device-id-jlmqxicb=1eafaacb-f18d-402a-8255-b763cf390df6; intercom-session-jlmqxicb=',
            'Origin': apainier('aHR0cHM6Ly93d3cuYmxhY2tib3guYWk=').decode("utf-8"),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return {"results": response.text, "join": "@Er_Support_Group", "success": True}
        except Exception as e:
            return e  

    async def kapan_libur(self):
        """
        Dapatkan informasi Hari libur kedepan.

        Returns:
            str: Hari Libur Berikutnya.
        """
        response = requests.get(self.base_urls["libur"]).json()
        next_libur = response["data"]["nextLibur"]
        return next_libur

    async def ambil_doa(self, nama_doa: str) -> str:
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

    async def cohere(self, pertanyaan: str) -> str:
        """
        Mengambil respons dari API AI ItzPire berdasarkan pertanyaan yang diberikan menggunakan metode POST.

        Args:
            pertanyaan (str): Teks pertanyaan yang akan dikirim ke AI.

        Returns:
            str: Respons yang dihasilkan oleh AI.
        """

        url = self.base_urls["ai_url"]
        params = {"q": pertanyaan}
        #     headers = {"Content-Type": "application/json"}  # Menentukan tipe konten sebagai JSON

        respons = await self._make_request(url, params=params)

        # ... (sisanya sama seperti kode sebelumnya)

        # Memastikan respons adalah dictionary dan memeriksa status keberhasilan
        if isinstance(respons, dict):
            if respons.get("status") == "success":
                # Mengambil hasil dari field 'result'
                result = respons.get("result", "Tidak ada hasil dari AI.")
                return result
            else:
                return "Status API menunjukkan kegagalan."
        else:
            return "Format respons tidak valid atau terjadi kesalahan."

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

    async def github_search(self, query, search_type="repositories", max_results=3):
        """
        Pencarian GitHub untuk beberapa tipe konten.

        Args:
            query (str): query Pencarian.
            search_type (str, optional): Type pencarian, terdiri dari:
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
        valid_search_types = [
            "repositories",
            "users",
            "organizations",
            "issues",
            "pull_requests",
            "commits",
            "topics",
        ]

        if search_type not in valid_search_types:
            return {
                "error": f"Type pencarian salah guoblok. Tipe validnya kek gini: {valid_search_types}"
            }

        url_mapping = {
            "pull_requests": "https://api.github.com/search/issues",
            "organizations": "https://api.github.com/search/users",
            "topics": "https://api.github.com/search/topics",
        }

        if search_type in url_mapping:
            url = url_mapping[search_type]
            if search_type == "pull_requests":
                query += " type:pr"
            elif search_type == "organizations":
                query += " type:org"
        else:
            url = f"https://api.github.com/search/{search_type}"

        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            items = results.get("items", [])

            result_list = []

            for item in items:
                item_info = {}
                if search_type == "repositories":
                    item_info = {
                        "name": item["name"],
                        "full_name": item["full_name"],
                        "description": item["description"],
                        "url": item["html_url"],
                        "language": item.get("language"),
                        "stargazers_count": item.get("stargazers_count"),
                        "forks_count": item.get("forks_count"),
                    }
                elif search_type in ["users", "organizations"]:
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
                elif search_type in ["issues", "pull_requests"]:
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
                elif search_type == "commits":
                    item_info = {
                        "sha": item["sha"],
                        "commit_message": item["commit"]["message"],
                        "author": item["commit"]["author"]["name"],
                        "date": item["commit"]["author"]["date"],
                        "url": item["html_url"],
                    }
                elif search_type == "topics":
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
            amount (int): Jumlah gambar nya, Defaultnya 1.

        Returns:
            list: List dari dictionaries tentang informasi neko image atau GIF.
                  Type dictionaries:
                  - anime_name (str): Nama anime.
                  - url (str): Url gif nya.
        """
        response = await self._make_request(self.base_urls["neko_hug"].format(amount))
        return response["results"]


apinya = ErApi()
