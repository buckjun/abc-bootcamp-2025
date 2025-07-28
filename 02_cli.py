from dotenv import load_dotenv
load_dotenv() # .env 파일이 존재한다면, 환경변수로서 로딩. 없다고 오류나지는 않음

import os
API_KEY = os.environ["OPENAI_API_KEY"]



from openai import OpenAI
client = OpenAI(api_key = API_KEY)  # OPENAI_API_KEY 환경변수 지정이 필요

response = client.responses.create(
    model="gpt-4o",
    input="make python code for trillogy",
)

print("usage :", response.usage)
print(response.output_text)
