import requests

page_url = "https://www.melon.com/chart/age/list.htm"

params = {
    "idx": "1",
    "chartType": "YE",
    "chartGenre": "KPOP",
    "chartDate": "2019",
    "moved": "Y",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

res = requests.get(page_url, params = params, headers = headers)
print(res) #상태 코드 출력


# crawling 폴더 내부에 파일 저장
import os
crawling_dir = os.path.dirname(os.path.abspath(__file__))
dump_path = os.path.join(crawling_dir, "melon_dump.html")
json_path = os.path.join(crawling_dir, "melon_kpop_2019.json")

html: str = res.text
with open(dump_path, "wt", encoding="utf-8") as f:
    f.write(html)
    print("written to", f.name)

# --- BeautifulSoup4로 melon_dump.html 파싱 및 JSON 저장 ---
from bs4 import BeautifulSoup
import json

with open(dump_path, "rt", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

song_list = []
for tr in soup.select("tr.lst50"):
    # 순위
    rank_tag = tr.select_one("span.rank")
    rank = rank_tag.text.strip() if rank_tag else None

    # 곡명
    title_tag = tr.select_one("div.ellipsis.rank01 strong a")
    title = title_tag.text.strip() if title_tag else None

    # 가수명
    artist_tag = tr.select_one("div.ellipsis.rank02 a")
    artist = artist_tag.text.strip() if artist_tag else None

    # 앨범명 (img alt에서 추출)
    album_img = tr.select_one("td > div > a.image_type15 > img")
    album = None
    if album_img and album_img.has_attr("alt"):
        album = album_img["alt"].replace(" 앨범 이미지", "").strip()

    # 곡 id (onclick 속성에서 추출)
    song_id = None
    song_a = tr.select_one("div.ellipsis.rank01 strong a")
    if song_a and song_a.has_attr("href"):
        import re
        m = re.search(r"playSong\('[^']*','(\d+)'\)", song_a["href"])
        if m:
            song_id = m.group(1)

    # 앨범 id (onclick 속성에서 추출)
    album_id = None
    album_span = tr.select_one("span.bg_album_frame")
    if album_span and album_span.has_attr("onclick"):
        m = re.search(r"goAlbumDetail\('(\d+)'\)", album_span["onclick"])
        if m:
            album_id = m.group(1)

    song_list.append({
        "rank": rank,
        "title": title,
        "artist": artist,
        "album": album,
        "song_id": song_id,
        "album_id": album_id
    })

with open(json_path, "wt", encoding="utf-8") as f:
    json.dump(song_list, f, ensure_ascii=False, indent=4)
    print("written to", f.name)

