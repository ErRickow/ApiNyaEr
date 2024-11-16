import os
import random
import string
from os.path import realpath
from typing import Union

import aiofiles
import aiohttp
import requests

from .fungsi import FilePath


class ErApi:
    def __init__(self):
        self.base_urls = {
            "neko_url": "https://nekos.best/api/v2/{endpoint}?amount={amount}",
            "neko_hug": "https://nekos.best/api/v2/hug?amount={}",
            "doa_url": "https://itzpire.com/religion/islamic/doa",
            "ai_url": "https://itzpire.com/ai/cohere",
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

        Argumen:
            url (str): URL tujuan permintaan dikirimkan.
            method (str, opsional): Metode HTTP yang digunakan (misalnya, "GET", "POST"). Default: "GET".
            params (dict, opsional): Parameter kueri yang disertakan dalam permintaan. Default: None.
            data (dict, opsional): Data yang disertakan dalam body permintaan (untuk permintaan POST). Default: None.
            files (dict, opsional): File yang diunggah dalam permintaan (jika ada). Default: None.
            headers (dict, opsional): Header yang disertakan dalam permintaan. Default: None.
            verify (bool, opsional): Apakah sertifikat SSL harus diverifikasi. Default: True.

        Mengembalikan:
            Union[dict, str]: Respons JSON dalam bentuk dictionary jika respons diformat sebagai JSON,
                              jika tidak, mengembalikan respons sebagai string.

        Menghasilkan:
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

    def _rnd_str(self):
        """
        Generates a random string of 8 alphanumeric characters.

        Returns:
            str: A random 8-character alphanumeric string.
        """
        random_str = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        return random_str

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
        Mengambil respons dari API AI ItzPire berdasarkan pertanyaan yang diberikan.

        Args:
            pertanyaan (str): Teks pertanyaan yang akan dikirim ke AI.

        Returns:
            str: Respons yang dihasilkan oleh AI.
        """
        url = self.base_urls["ai_url"]
        params = {"q": pertanyaan}
        respons = await self._make_request(url, params=params)

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
        Generates a code snippet image using the Carbon API, saves it to the downloads folder,
        uploads it, and returns the URL of the uploaded image.

        Args:
            query (str): The code snippet to be rendered as an image.

        Returns:
            FilePath: The file path of the saved image.
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
        Searches GitHub for various types of content.

        Args:
            query (str): The search query.
            search_type (str, optional): The type of search. Can be one of:
                - "repositories"
                - "users"
                - "organizations"
                - "issues"
                - "pull_requests"
                - "commits"
                - "topics"

                Defaults to "repositories".
            max_results (int, optional): The maximum number of results to return. Defaults to 3.

        Returns:
            list: A list of search results or an error message.
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
                "error": f"Invalid search type. Valid types are: {valid_search_types}"
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
            return {"error": f"Request exception: {e}"}
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
        Fetches a random cat image URL.

        Returns:
            str or None: The URL of a random cat image if available; None if no response is received.
        """
        response = await self._make_request(self.base_urls["cat"])
        return response[0]["url"] if response else None

    async def dog(self):
        """
        Fetches a random dog image URL.

        Returns:
            str or None: The URL of a random dog image if available; None if no response is received.
        """
        response = await self._make_request(self.base_urls["dog"])
        return response["url"] if response else None

    async def hug(self, amount: int = 1) -> list:
        """Fetches a specified number hug gif from the Nekos.Best API.

        Args:
            amount (int): The number of neko images to fetch. Defaults to 1.

        Returns:
            list: A list of dictionaries containing information about each fetched neko image or GIF.
                  Each dictionary typically includes:
                  - anime_name (str): The name of the anime.
                  - url (str): The URL of the GIF.
        """
        response = await self._make_request(self.base_urls["neko_hug"].format(amount))
        return response["results"]


apinya = ErApi()
