

---

### Test Results

| Function | Status | Result |
|---|---|---|
| ErApi.neko(neko, 3) | ✅ | {'results': [{'artist_href': 'https://www.pixiv.net/en/users/28603589', 'artist_name': '木塘ムタン', 'source_url': 'https://www.pixiv.net/en/artworks/80228378', 'url': 'https://nekos.best/api/v2/neko/fa4c8d73-6e90-47d2-bae8-49c06f0845ad.png'}, {'artist_href': 'https://www.pixiv.net/en/users/11683125', 'artist_name': 'KeenH', 'source_url': 'https://www.pixiv.net/en/artworks/79753379', 'url': 'https://nekos.best/api/v2/neko/d25c8cb7-69d3-4672-9947-1073a60f9083.png'}, {'artist_href': 'https://www.pixiv.net/en/users/27591308', 'artist_name': 'RK', 'source_url': 'https://www.pixiv.net/en/artworks/100438383', 'url': 'https://nekos.best/api/v2/neko/2409e8cf-0104-49e2-80c8-debb0dde3d81.png'}]} |
| ErApi.neko(neko, 2) | ✅ | {'results': [{'artist_href': 'https://www.pixiv.net/en/users/26549122', 'artist_name': 'Ao', 'source_url': 'https://www.pixiv.net/en/artworks/86996647', 'url': 'https://nekos.best/api/v2/neko/ac93c988-2c60-4765-a6db-c4a8e74e422d.png'}, {'artist_href': 'https://www.pixiv.net/en/users/2550839', 'artist_name': 'みなみさき', 'source_url': 'https://www.pixiv.net/en/artworks/87122035', 'url': 'https://nekos.best/api/v2/neko/aea0203e-aae4-420a-97e7-62e3bb4f3261.png'}]} |
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