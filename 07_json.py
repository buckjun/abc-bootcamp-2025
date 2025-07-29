import json
import requests

url = "https://pyhub.kr/melon/20231204.json"

response = requests.get(url)
print(response)

# string -> object : deserialize (역직렬화) 문자열은 뽑을때 한자한자씩 뽑으니 뭉텡이로 묶어놓는것
json_string:str = response.text
response_obj = json.loads(json_string)
print(type(response_obj))
print(len(response_obj))

for song in response_obj:
    print(song["곡명"], song["가수"])
    