

---

### Test Results

| Function | Status | Result |
|---|---|---|
| ErApi.neko(neko, 3) | ✅ | {'results': [{'artist_href': 'https://www.pixiv.net/en/users/70194544', 'artist_name': 'Ham', 'source_url': 'https://www.pixiv.net/en/artworks/103077987', 'url': 'https://nekos.best/api/v2/neko/a85811fe-04e6-4079-a7eb-965e59c290aa.png'}, {'artist_href': 'https://www.pixiv.net/en/users/39711325', 'artist_name': 'ななのめ', 'source_url': 'https://www.pixiv.net/en/artworks/99045708', 'url': 'https://nekos.best/api/v2/neko/87758264-0ec0-4624-ae1a-22b4d026c79f.png'}, {'artist_href': 'https://www.pixiv.net/en/users/14089200', 'artist_name': '抹茶Amigo', 'source_url': 'https://www.pixiv.net/en/artworks/93455209', 'url': 'https://nekos.best/api/v2/neko/45f32f99-924e-430c-9db8-8c865f4fb77d.png'}]} |
| ErApi.neko(neko, 2) | ✅ | {'results': [{'artist_href': 'https://www.pixiv.net/en/users/53862745', 'artist_name': 'ひなた', 'source_url': 'https://www.pixiv.net/en/artworks/92705462', 'url': 'https://nekos.best/api/v2/neko/ef806e93-531b-41a1-a6b6-93fb5b5ef46f.png'}, {'artist_href': 'https://www.pixiv.net/en/users/2257693', 'artist_name': 'こもも', 'source_url': 'https://www.pixiv.net/en/artworks/93139156', 'url': 'https://nekos.best/api/v2/neko/2d907553-a4a6-43e1-90d9-11d82c444243.png'}]} |
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