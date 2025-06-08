"""
LLM이 정책 정보를 정확히 이해하고 응답할 수 있도록,
비정형 텍스트를 구조화된 프롬프트 형식으로 전처리하는 파이프라인
"""

# %% [1] 모듈 임포트
import pandas as pd
from pathlib import Path
import os
import datetime

# %% [2] 데이터 로드
INPUT_PATH = Path("1.data/20250304.csv")
df = pd.read_csv(INPUT_PATH)

# %% [3] 분석 보류 컬럼 포함해서 필요한 컬럼 필터링
keep_cols = [
    "등록일시", "사용자구분",
    "서비스ID", "서비스명", "서비스목적요약", "선정기준", "소관기관명", "소관기관유형",
    "신청기한", "신청방법", "지원내용", "지원대상", "지원유형"
]
df = df[keep_cols]

# %% [4] 텍스트 정제 함수 정의
def clean_text(text):
    return str(text).replace("\n", " ").replace("\r", " ").strip()

# %% [5] 프롬프트 생성 함수
def make_prompt(row):
    title = clean_text(row["서비스명"])
    content = "\n".join(
        f"{col}: {clean_text(row.get(col, ''))}"
        for col in ["지원대상", "지원내용", "신청기한", "신청방법", "전화문의", "출처"]
    )
    return {
        "서비스ID": row["서비스ID"],
        "제목": title,
        "본문": content
    }

prompt_df = pd.DataFrame([make_prompt(row) for _, row in df.iterrows()])

# %% [6] 저장
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

output_file = f"{timestamp}_prompt_ready.csv"
prompt_df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"✅ 프롬프트 데이터셋 저장 완료: {output_file}")

# %%
