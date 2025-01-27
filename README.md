

---

### Test Results

| Function | Status | Result |
|---|---|---|
| ErApi.neko(neko, 3) | ✅ | {'results': [{'artist_href': 'https://twitter.com/kurorakudaaa', 'artist_name': '紙守くーらく', 'source_url': 'https://twitter.com/kurorakudaaa/status/1515268879962222597', 'url': 'https://nekos.best/api/v2/neko/f06ded23-5895-4786-9daa-e88e42477b25.png'}, {'artist_href': 'https://www.pixiv.net/en/users/43054314', 'artist_name': '鈴崎', 'source_url': 'https://www.pixiv.net/en/artworks/92510405', 'url': 'https://nekos.best/api/v2/neko/be1bef84-1789-40ec-b67d-a9287b82dc39.png'}, {'artist_href': 'https://www.pixiv.net/en/users/23677411', 'artist_name': '東雲あす', 'source_url': 'https://www.pixiv.net/en/artworks/79396842', 'url': 'https://nekos.best/api/v2/neko/13b15c2d-1e44-4968-9e9b-42872a283e0d.png'}]} |
| ErApi.neko(neko, 2) | ✅ | {'results': [{'artist_href': 'https://www.pixiv.net/en/users/221597', 'artist_name': 'はみこ', 'source_url': 'https://www.pixiv.net/en/artworks/78785775', 'url': 'https://nekos.best/api/v2/neko/1c7a632e-5d18-45cd-af54-28e2c2f289de.png'}, {'artist_href': 'https://www.pixiv.net/en/users/24563064', 'artist_name': 'カメレオン', 'source_url': 'https://www.pixiv.net/en/artworks/97964073', 'url': 'https://nekos.best/api/v2/neko/ad1ac202-987f-4892-b7dc-dc3398a080c1.png'}]} |
| Musiknya.search(Gue Mah Apah) | ✅ | {'success': False, 'message': 'Unexpected token \'<\', "<!DOCTYPE "... is not valid JSON'} |
| Musiknya.get_song_by_id(some_song_id) | ✅ | {'success': False, 'message': 'Unexpected token \'<\', "<!DOCTYPE "... is not valid JSON'} |

### File Structure

```

    ApiNyaEr/
    ├── __init__.py
    ├── erapi.py
    ├── musiknya.py
    └── utils.py
    
```


> This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)