# %% [1] 모듈 임포트 및 환경 설정
import pandas as pd
from pathlib import Path
import json
from datetime import datetime
import os
import re
from dotenv import load_dotenv

# %% [2] 데이터 불러오기
input_path = Path("1.data/20250608_170314_prompt_ready.csv")

if not input_path.exists():
    print(f"❌ 파일이 존재하지 않습니다: {input_path.resolve()}")
    exit(1)

df = pd.read_csv(input_path)

# %% [3] 환경 변수 로드
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM 설정 (주석처리해둠, 실사용 시 해제)
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
# from langchain.schema import SystemMessage
# llm_summarize = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, api_version="v1", temperature=0)
# chat_openai = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, api_version="v1", temperature=0)

# %% [4] 프롬프트 생성 함수 (사용 안 함 – 주석처리)
"""
def process_data(title, content):
    chat_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="(프롬프트 내용 생략 – 너는 알잖아. 길다구.)"),
        HumanMessagePromptTemplate.from_template(\"""제목: {title} 본문: {content} …\""")
    ])
    messages = chat_template.format_messages(title=title, content=content)
    return messages
"""

# %% [5] 텍스트 정제 함수
# def clean_text(text):
#     if text is None:
#         return ""
#     text = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣A-Za-z0-9\s\-\~\<\>\.\:\/\@\%\+\*\#\°\₩\$]', '', text)
#     text = re.sub(r'[\n\r]', ' ', text)
#     text = text.lower().strip()
#     return text
def clean_text(text):
    if pd.isnull(text):
        return ""
    if not isinstance(text, str):
        text = str(text)
    
    # 특수문자 제거: 한글, 영문, 숫자, 기본적인 기호만 허용
    text = re.sub(r"[^ㄱ-ㅎ가-힣a-zA-Z0-9\s.,!?/:()\-]", "", text)

    # 줄바꿈 문자 제거
    text = re.sub(r'[\n\r\t]+', ' ', text)

    # 공백 정리
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip().lower()


def clean_keywords(text):
    if pd.isnull(text):
        return ""
    if not isinstance(text, str):
        text = str(text)

    # 괄호 포함 제거 + 특수문자 제거 + 공백 정리
    text = re.sub(r'[\(\)\[\]\{\}<>]', '', text)  # 괄호류 제거
    text = re.sub(r'[^ㄱ-ㅎ가-힣a-zA-Z0-9\s]', '', text)  # 나머지 특수문자 제거
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()

# %% [6] 가짜 LLM 응답 생성 함수
def fake_llm_response(title, content):
    cleaned_content = clean_text(content)
    return {
        "area": "전국",
        "district": "",
        "min_age": 0,
        "max_age": 99,
        "age_summary": "",
        "gender": "",
        "income_category": "",
        "income_summary": "",
        "personal_category": "",
        "personal_summary": "",
        "household_category": "",
        "household_summary": "",
        "support_type": "기타",
        "support_summary": "",
        "application_method": "온라인 신청",
        "application_summary": "",
        "benefit_category": "생활안정",
        "benefit_summary": "",
        "start_date": "",
        "end_date": "",
        "date_summary": "",
        "benefit_details": cleaned_content[:100],
        "source": "모름",
        "additional_data": "아니오",
        "keywords": [clean_keywords(kw) for kw in title.split()[:3]]  # 정제 적용
    }

# %% [7] 응답 생성 루프
results = []
for _, row in df.iterrows():
    title = row["제목"]
    content = row["본문"]
    service_id = row["서비스ID"]

    result = fake_llm_response(title, content)
    result["서비스ID"] = service_id
    results.append(result)

# %% [8] 결과 저장
output_dir = Path("2.llm_result")
output_dir.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# JSON 저장
output_json = output_dir / f"{timestamp}_llm_result.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

# CSV 저장도 덤으로
pd.DataFrame(results).to_csv(output_dir / f"{timestamp}_llm_result.csv", index=False, encoding="utf-8-sig")

print(f"✅ 결과 저장 완료 (JSON): {output_json}")
