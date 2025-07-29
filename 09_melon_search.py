import json
import time
import requests

def melon_search(query:str):
    search_url = "https://www.melon.com/search/keyword/index.json"

    #Query parameter for search ?로 구분
    params = {
        "jscallback": "_",
        "query": "idol",
        "_": int(time.time()),
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    res = requests.get(search_url, params=params, headers=headers)
    

    if res.status_code == 200:
        # response format : json 이면서 jsonp 형식으로 받아짐
        jsonp_string = res.text
        json_string = jsonp_string[2:-2]
        return json.loads(json_string)
    return []

#현재 소스파일이 파이썬의 진입점일 떼
if __name__ == "__main__":
    print(melon_search("idol"))
