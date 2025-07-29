
# ABC Bootcamp 2025 프로젝트

## 개요

이 프로젝트는 데이터 부트캠프 실습 과정에서 생성된 결과물입니다.
파이썬 3.13 버전과 Anaconda Python을 이용한 가상환경에서 개발 및 실행되었습니다.
다양한 Python 예제와 AI, 웹앱, CLI, 오디오 처리, 멜론 차트 데이터 활용 등 실습을 포함합니다. OpenAI API, Streamlit, gTTS, pygame, requests 등 다양한 라이브러리를 활용합니다.

## 폴더 및 파일 구조

- `01_cli.py` : 간단한 Python CLI 예제 ("hello python" 출력)
- `02_cli.py` : OpenAI API를 이용한 텍스트 생성 CLI
- `03_cli.py` : 얼굴 특징을 입력받아 AI 관상 분석 결과를 출력하는 CLI
- `04_webapp.py` : Streamlit 기반 AI 관상 분석 웹앱
- `05_cli_streaming.py` : OpenAI API의 스트리밍 응답을 CLI에서 출력
- `06_cli_chat.py` : OpenAI API를 활용한 한국어 상황극(챗봇) CLI
- `07_json.py` : 멜론 차트 JSON 데이터 파싱 및 출력 예제
- `08_webapp_melon_top100.py` : 멜론 TOP100 차트 웹앱 (Streamlit)
- `09_melon_search.py` : 멜론 검색 API 활용 예제
- `10_melon_vive_vinilization.html` : (빈 파일, 추후 확장 가능)
- `ai.py` : OpenAI API를 통한 관상 분석 함수 정의
- `audio.py` : gTTS와 pygame을 이용한 음성 합성 및 재생 함수
- `generator_01.py` : 파이썬 generator 예제
- `html/01_melon_top100.html` : 멜론 TOP100 차트 결과 HTML 예제
- `requirements.txt` : 프로젝트 의존성 패키지 목록


## 개발 환경

- Python 3.13 (Anaconda 가상환경 사용)
- Windows OS 기준

### 가상환경 생성 및 활성화 예시 (Anaconda)
```bash
conda create -n abc2025 python=3.13
conda activate abc2025
```

## 주요 라이브러리 및 의존성

`requirements.txt`에 정의된 주요 패키지:

- openai
- python-dotenv
- streamlit
- gtts
- pygame
- requests
- httpx


설치 방법:
```bash
pip install -r requirements.txt
# 또는 아나콘다 환경에서
conda install --file requirements.txt
```

## 실행 방법

### 1. CLI 예제 실행
```bash
python 01_cli.py
python 02_cli.py
python 03_cli.py
python 05_cli_streaming.py
python 06_cli_chat.py
```

### 2. 웹앱 실행
```bash
streamlit run 04_webapp.py
streamlit run 08_webapp_melon_top100.py
```

### 3. 기타 예제
```bash
python 07_json.py
python 09_melon_search.py
python generator_01.py
```

## 환경 변수

OpenAI API를 사용하려면 `.env` 파일에 아래와 같이 API 키를 설정해야 합니다.

```
OPENAI_API_KEY=your_openai_api_key
```

## 참고

- 일부 예제는 인터넷 연결이 필요합니다.
- 멜론 API 사용 시, 실제 서비스 정책에 따라 접근이 제한될 수 있습니다.

---
문의: buckjun
