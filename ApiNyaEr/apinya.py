import os
import re
import random
import string
from base64 import b64decode as apainier
from typing import Union, Optional

import aiofiles

from .td import DARE, TRUTH
from ._req import Reqnya
from .teks import EPEP, PUBG, FAKTA, ANIMEK, HECKER, ISLAMIC


class ErApi:
    """
    A class to interact with various APIs and perform operations like fetching data and generating files.

    Args:
        downloads_dir (``str``, *optional*): Directory to save downloaded files. Defaults to "downloads".
        quiet (``bool``, *optional*): Whether to suppress error messages. Defaults to False.
    """

    def __init__(self, downloads_dir: str = "downloads", quiet: bool = False):
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
        self._make_request = Reqnya()
        self.downloads_dir = downloads_dir
        self.quiet = quiet

        os.makedirs(self.downloads_dir, exist_ok=True)

    def _handle_error(self, error: Exception) -> Union[dict, Exception]:
        if self.quiet:
            return {"error": True, "message": str(error)}
        raise error

    async def _create_file(
        self, contents: bytes, ext: str, name: Optional[str] = None
    ) -> str:
        file_name = f"{name or 'file'}_{self._rnd_str()}.{ext}"
        file_path = os.path.join(self.downloads_dir, file_name)

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(contents)

        return file_path

    async def neko(self, endpoint: str = "neko", amount: int = 3) -> dict:
        """Fetches a specified number of neko images or GIFs from the Nekos.Best API.

        Args:
            endpoint (``str``): The endpoint category to fetch content from. Default is "neko".
                Valid image endpoints:
                **"husbando"**, **"kitsune"**, **"neko"**, **"waifu"**
                Valid GIF endpoints:
                **"baka"**, **"bite"**, **"blush"**, **"bored"**, **"cry"**, **"cuddle"**,
                **"dance"**, **"facepalm"**, **"feed"**, **"handhold"**, **"handshake"**,
                **"happy"**, **"highfive"**, **"hug"**, **"kick"**, **"kiss"**, **"laugh"**,
                **"lurk"**, **"nod"**, **"nom"**, **"nope"**, **"pat"**, **"peck"**, **"poke"**,
                **"pout"**, **"punch"**, **"shoot"**, **"shrug"**, **"slap"**, **"sleep"**,
                **"smile"**, **"smug"**, **"stare"**, **"think"**, **"thumbsup"**, **"tickle"**,
                **"wave"**, **"wink"**, **"yawn"**, **"yeet"**
            amount (``int``): The number of items to fetch. Default is 3.

        Returns:
            ``dict``: A dictionary containing the results of the request. The dictionary has a key
            **"results"**, which holds a list of items.
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
            return self._handle_error(
                ValueError(
                    f"Invalid endpoint '{endpoint}'. Must be one of: {', '.join(valid_categories)}"
                )
            )

        url = self.base_urls["neko_url"].format(endpoint=endpoint, amount=amount)

        response = await self._make_request.get(url)

        return response.json()

    async def password(num: int = 12) -> str:
        """
        Fungsi ini menghasilkan kata sandi acak dengan menggabungkan huruf besar, huruf kecil, tanda baca, dan digit.

        Parameters:
            - num (``int``): Panjang kata sandi yang dihasilkan. Default adalah 12 jika tidak ditentukan.

        Returns:
            - ``str``: Kata sandi yang dihasilkan secara acak yang terdiri dari karakter dari string.ascii_letters, string.punctuation, dan string.digits.
        """
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(random.sample(characters, num))
        return password

    def _rnd_str(self) -> str:
        random_str = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        return random_str

    async def truth():
        """
        Dapatkan Kata kata truth

        Returns:
            ``str``: Random kata truth
        """
        truthnya = random.choice(TRUTH)
        return truthnya

    async def qanime():
        """
        Dapatkan Kata kata anime

        Returns:
            ``str``: Random kata anime
        """
        mmk = random.choice(ANIMEK)
        return mmk

    async def dare():
        """
        Dapatkan Kata kata dare

        Returns:
            ``str``: Random kata dare
        """
        darenya = random.choice(DARE)
        return darenya

    async def nama_epep():
        """
        Dapatkan random nama ep ep

        Returns:
            ``str``: Random nama ep epnya
        """
        namanya = random.choice(EPEP)
        return namanya

    async def qpubg():
        """
        Dapatkan random Quotes pubg

        Returns:
            ``str``: Random Quotes Pubg
        """
        kntlny = random.choice(PUBG)
        return kntlny

    async def qhacker():
        """
        Dapatkan random Quotes Hacker

        Returns:
            ``str``: Random Quotes Hacker
        """
        mmk = random.choice(HECKER)
        return mmk

    async def qislam():
        """
        Dapatkan random Quotes Islamic

        Returns:
            ``str``: Random Quotes Islam
        """
        Sabyan = random.choice(ISLAMIC)
        return Sabyan

    async def fakta_unik():
        """
        Dapatkan random Seputar Fakta Unik

        Returns:
            ``str``: Random Fakta
        """
        kntlny = random.choice(FAKTA)
        return kntlny

    async def arti_nama(self, namanya: str):
        """
        Mendapatkan arti nama dari string

        Args:
            namanya (``str``): Nama Kamu
        Returns:
            ``dict``: Informasi Arti Nama Kamu or Eror Msg
        """
        url = f"{self.base_urls['siputx']}/primbon/artinama"
        par = {"nama": namanya}
        try:
            res = await self._make_request.get(url, params=par)
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
                "Why?": f"Terjadi kesalaha",
                "success": False,
                "report": "@Er_Support_Group",
            }

    async def zodiak(self, input: str):
        """
        Mengambil informasi zodiak berdasarkan input.

        Args:
            input (``str``): Nama zodiak.

        Returns:
            ``dict``: Informasi lengkap zodiak atau pesan kesalahan.
        """
        url = f"{self.base_urls['siputx']}/primbon/zodiak"
        par = {"zodiak": input}
        try:
            res = await self._make_request.get(url, params=par)
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
                "Why?": f"Terjadi kesalahan",
                "success": False,
                "report": "@Er_Support_Group",
            }

    async def read_image(self, urlnya: str):
        """
        Bertanya gambar melalui url

        Returns:
            url(``str``): string url
        Returns:
            ``Response``: Response ainya
        """
        url = f"{self.base_urls['siputx']}/ai/image2text"
        urlnya = "https://cataas.com/cat"
        par = {"url": urlnya}
        try:
            res = await self._make_request.get(url, params=par)
            if res["status"] is True:
                return {
                    "resultnya": res["data"],
                    "from": "ApiNyaEr",
                    "success": True,
                }
        except Exception as r:
            return {
                "resultnya": False,
                "why?": "Response Sedang Eror kAk, silahkan coba lagi nanti",
                "report": "@Er_Support_Group",
            }

    async def meta_ai(self, tanya: str):
        """
        Bertanya pada meta AI

        Args:
            tanya(``str``): teks yang akan ditanyakan
        Returns:
            ``response``: Response Meta Ai
        """
        url = f"{self.base_urls['siputx']}/ai/metaai"
        par = {"query": tanya}
        try:
            res = await self._make_request.get(url, params=par)
            if res["status"] is True:
                return {
                    "resultnya": res["data"],
                    "from": "ApiNyaEr",
                    "success": True,
                }
        except Exception as r:
            return {
                "resultnya": False,
                "why?": "Response Sedang Eror kAk, silahkan coba lagi nanti",
                "report": "@Er_Support_Group",
            }

    async def fluxai(self, input: str):
        """
        Generate image from Teks

        Returns:
            ``input``: teks yang akan dijadikan image
        """
        params = {"prompt": input}
        try:
            res = await self._make_request.get(self.base_urls["flux"], params=params)
            return res
        except Exception as r:
            return {
                "resultnya": False,
                "why?": "Response Sedang Eror kAk, silahkan coba lagi nanti",
                "report": "@Er_Support_Group",
            }

    async def terabox_dl(self, link: str):
        """
        Args:
            link (``str``): Teks query

        Returns:
            ``resultnya``
        """
        params = {"url": link}
        try:
            response = await self._make_request.get(
                self.base_urls["njir"], params=params
            )
            if response["data"]:
                return {
                    "judul": response["data"]["filename"],
                    "ukuran": response["data"]["size"],
                    "url": response["data"]["download"],
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as e:
            return {
                "resultnya": False,
                "why?": "Response Sedang Eror kAk, silahkan coba lagi nanti",
                "report": "@Er_Support_Group",
            }

    async def islam_ai(self, tanya: str):
        """
        args:
            tanya (``str``): teks pertanyaan

        Returns:
            ``resultnya``: Response islam ai
        """
        paman = {"q": tanya}
        try:
            res = await self._make_request.get(self.base_urls["whe"], params=paman)
            if res["status"] == True:
                return {
                    "resultnya": res["result"],
                    "from": "ApiNyaEr",
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as r:
            return {
                "resultnya": False,
                "why?": "Response Sedang Eror kAk, silahkan coba lagi nanti",
                "report": "@Er_Support_Group",
            }

    async def luminai(self, tanya: str):
        """
        Args:
            tanya (``str``): Teks query

        Returns:
            ``resultnya``: Response luminai
        """
        params = {"text": tanya}
        try:
            response = await self._make_request.get(
                self.base_urls["luminai"], params=params
            )
            if response["data"]:
                return {
                    "resultnya": response["data"]["result"],
                    "join": "@Er_Support_Group",
                    "success": True,
                }
        except Exception as e:
            return {
                "resultnya": False,
                "why?": "Response Luminai Sedang Eror kAk, silahkan coba lagi nanti",
                "report": "@Er_Support_Group",
            }

    async def ai(self, tanya: str):
        """
        Interaksi dengan AI Basis Text.

        Args:
            tanya (``str``): Text inputnya.

        Returns:
            ``str``: Respon chatbotnya.
        """
        url = self.base_urls["ai"]
        par = {"q": tanya}
        try:
            res = await self._make_request.get(url, params=par)
            if res["status"] == True:
                return {
                    "resultnya": res["result"],
                    "from": "ApiNyaEr",
                    "join": "@Er_Support_Group",
                }
        except Exception:
            return {
                "resultnya": False,
                "Why?": "Response Sedang Error",
                "report": "@Er_Support_Group",
            }

    async def doa(self, nama_doa: str) -> str:
        """
        Mengambil data doa dari API ItzPire berdasarkan nama doa.

        Args:
            nama_doa (``str``): Nama doa yang ingin diambil.

        Returns:
            ``str``: Teks doa yang diformat dengan rapi termasuk doa, ayat, latin, dan artinya.
        """
        url = self.base_urls["doa_url"]
        params = {"doaName": nama_doa}
        respons = await self._make_request.get(url, params=params)

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

    async def bing_image(self, query: str, limit: int = 3, adlt: str = "moderate"):
        """
        Searches Bing for images based on a query and retrieves image URLs.

        Args:
            query (``str``): The search query string for finding images.
            limit (``int``, *optional*): The maximum number of image URLs to return. Defaults to 3.
            adlt (``str``, *optional*): The level of adult content filtering to apply.
                The available options are:
                "off", which disables filtering for adult content.
                "moderate" (default), which filters explicit images but may include related content.
                "strict", which enforces strict filtering, excluding all adult content.

        Returns:
            ``list``: A list of image URLs retrieved from the Bing search results.
        """
        data = {
            "q": query,
            "first": 0,
            "count": limit,
            "adlt": adlt,
            "qft": "",
        }
        response = await self._make_request.get(
            self.base_urls["bing_image"], params=data
        )
        return (
            re.findall(r"murl&quot;:&quot;(.*?)&quot;", response.text)
            if response
            else []
        )

    async def carbon(
        self,
        code,
        background_color="rgba(171, 184, 195, 1)",
        drop_shadow=True,
        drop_shadow_blur_radius="68px",
        drop_shadow_offset_y="20px",
        export_size="2x",
        font_custom="",
        font_size="14px",
        font_family="Hack",
        first_line_number=1,
        language="auto",
        line_height="133%",
        line_numbers=False,
        padding_horizontal="56px",
        padding_vertical="56px",
        prettify=False,
        selected_lines="",
        theme="seti",
        watermark=False,
        width=536,
        width_adjustment=True,
        window_controls=True,
        window_theme="none",
    ):
        """
        Generate an image of a code snippet using the `Carbonara API <https://github.com/petersolopov/carbonara>`_.


        Args:
            code (``str``): **Required.** The code snippet to generate an image for.
            background_color (``str``, *optional*): Background color of the image. Can be in ``rgba`` or ``hex`` format. Default is ``"rgba(171, 184, 195, 1)"``.
            drop_shadow (``bool``, *optional*): Whether to enable the shadow effect. Default is ``True``.
            drop_shadow_blur_radius (``str``, *optional*): The blur radius of the shadow. Default is ``"68px"``.
            drop_shadow_offset_y (``str``, *optional*): The vertical offset of the shadow. Default is ``"20px"``.
            export_size (``str``, *optional*): Resolution of the exported image, such as ``"1x"``, ``"2x"``, or ``"3x"``. Default is ``"2x"``.
            font_custom (``str``, *optional*): Custom font in Base64 format. Leave empty for default fonts. Default is an empty string.
            font_size (``str``, *optional*): The size of the font in the code snippet. Default is ``"14px"``.
            font_family (``str``, *optional*): Font family for the code snippet. Examples: ``"Hack"``, ``"JetBrains Mono"``, ``"Fira Code"``. Default is ``"Hack"``.
            first_line_number (``int``, *optional*): The line number to start with in the snippet. Default is ``1``.
            language (``str``, *optional*): Programming language for syntax highlighting. Default is ``"auto"``. Example: Use ``"python"``, ``"javascript"``, or ``"application/x-sh"`` for bash.
            line_height (``str``, *optional*): Line height for the text in the snippet. Default is ``"133%"``.
            line_numbers (``bool``, *optional*): Whether to display line numbers in the snippet. Default is ``False``.
            padding_horizontal (``str``, *optional*): Horizontal padding around the code block. Default is ``"56px"``.
            padding_vertical (``str``, *optional*): Vertical padding around the code block. Default is ``"56px"``.
            prettify (``bool``, *optional*): Automatically format JavaScript code using Prettier. Default is ``False``.
            selected_lines (``str``, *optional*): Specific lines to highlight, as a comma-separated string. Example: ``"3,4,6"``. Default is an empty string.
            theme (``str``, *optional*): The theme for the code snippet. Available themes:
                - "3024-night"
                - "a11y-dark"
                - "blackboard"
                - "base16-dark"
                - "base16-light"
                - "cobalt"
                - "duotone-dark"
                - "dracula-pro"
                - "hopscotch"
                - "lucario"
                - "material"
                - "monokai"
                - "nightowl"
                - "nord"
                - "oceanic-next"
                - "one-light"
                - "one-dark"
                - "panda-syntax"
                - "parasio-dark"
                - "seti"
                - "shades-of-purple"
                - "solarized+dark"
                - "solarized+light"
                - "synthwave-84"
                - "twilight"
                - "verminal"
                - "vscode"
                - "yeti"
                - "zenburn"
                Default is ``"seti"``.
            watermark (``bool``, *optional*): Whether to include the Carbon watermark. Default is ``False``.
            width (``int``, *optional*): Width of the image in pixels. Default is ``536``.
            width_adjustment (``bool``, *optional*): Automatically adjusts width based on content. Default is ``True``.
            window_controls (``bool``, *optional*): Show or hide window controls (close, minimize, maximize buttons). Default is ``True``.
            window_theme (``str``, *optional*): Style of the window controls. Options: ``"none"``, ``"sharp"``, ``"bw"``, ``"boxy"``. Default is ``"none"``.

        Returns:
            A dictionary containing either the file path to the generated image or an error message.
            If successful, the dictionary will contain **"success": True** and **"result"**: the file path where the generated image is saved.
            If failed, the dictionary will contain **"success": False** and **"error"**: a string describing the error that occurred.

        Example:
            .. code-block:: python

                code_snippet = "print('Hello, World!')"

                response = await api.carbon(
                    code_snippet,
                    theme="dracula",
                    language="python"
                )

                if response['success']:

                    print(f"Code image saved as '{response['result']}'.")

                else:

                    print(f"Error: {response['error']}")
        """

        payload = {
            "code": code,
            "backgroundColor": background_color,
            "dropShadow": drop_shadow,
            "dropShadowBlurRadius": drop_shadow_blur_radius,
            "dropShadowOffsetY": drop_shadow_offset_y,
            "exportSize": export_size,
            "fontCustom": font_custom,
            "fontSize": font_size,
            "fontFamily": font_family,
            "firstLineNumber": first_line_number,
            "language": language,
            "lineHeight": line_height,
            "lineNumbers": line_numbers,
            "paddingHorizontal": padding_horizontal,
            "paddingVertical": padding_vertical,
            "prettify": prettify,
            "selectedLines": selected_lines,
            "theme": theme,
            "watermark": watermark,
            "width": width,
            "widthAdjustment": width_adjustment,
            "windowControls": window_controls,
            "windowTheme": window_theme,
        }
        try:
            response = await self._make_request.post(
                self.base_urls["carbon"], json=payload
            )
            response.raise_for_status()
            file_path = await self._create_file(
                response.content, ext="png", name="carbon"
            )

            return {"success": True, "result": file_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def github_search(self, query, search_type="repositories", max_results=3):
        """
        Searches GitHub for various types of content.

        Args:
            query (``str``): The search query.
            search_type (``str``, *optional*): The type of search. Can be one of:
                - "repositories"
                - "users"
                - "organizations"
                - "issues"
                - "pull_requests"
                - "commits"
                - "topics"

                Defaults to "repositories".
            max_results (``int``, *optional*): The maximum number of results to return. Defaults to 3.

        Returns:
            ``list``: A list of search results or an error message.
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
            response = await self._make_request.get(url, headers=headers, params=params)
            response = response.json()
            items = response.get("items", [])

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

        except Exception as e:
            return self._handle_error(ValueError(f"Unexpected error: {e}"))

    async def cat(self):
        """
        Fetches a random cat image URL.

        Returns:
            ``str`` or ``None``: The URL of a random cat image if available; None if no response is received.
        """
        response = await self._make_request.get(self.base_urls["cat"])
        response = response.json()
        return response[0]["url"] if response else None

    async def dog(self):
        """
        Fetches a random dog image URL.

        Returns:
            ``str`` or None: The URL of a random dog image if available; None if no response is received.
        """
        response = await self._make_request.get(self.base_urls["dog"])
        response = response.json()
        return response["url"] if response else None

    async def hug(self, amount: int = 1) -> list:
        """Fetches a specified number hug gif from the Nekos.Best API.

        Args:
            amount (``int``): The number of neko images to fetch. Defaults to 1.

        Returns:
            ``list``: A list of dictionaries containing information about each fetched neko image or GIF.
                      Each dictionary will typically include:
                      **"anime_name"** (str): The name of the anime.
                      **"url"** (str): The URL of the GIF.

        """
        response = await self._make_request.get(
            self.base_urls["neko_hug"].format(amount)
        )

        return response.json()["results"]

    async def pypi(self, package_name):
        """
        Retrieves metadata information about a specified Python package from the PyPI API.

        Args:
            package_name (``str``): The name of the package to search for on PyPI.

        Returns:
            ``dict`` or ``None``: A dictionary with relevant package information if found.
            Returns None if the package is not found or there is an error.
        """
        url = f"{self.base_urls['pypi']}/{package_name}/json"
        response = await self._make_request.get(url)
        response = response.json()
        if response:
            return response
        else:
            return None
