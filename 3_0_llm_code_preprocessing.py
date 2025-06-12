# %% [1] 모듈 임포트 및 경로 설정
import pandas as pd
from pathlib import Path
from datetime import datetime
import re

# %% [2] 데이터 로드
input_path = Path("2.llm_result") / "20250612_140851_llm_result.json"
df = pd.read_json(input_path)

# %% [3] 텍스트 정제 함수
def normalize_date(date_str):
    try:
        return pd.to_datetime(date_str).strftime("%Y-%m-%d")
    except Exception:
        return ""

def clean_text(text):
    if text is None:
        return ""
    text = re.sub(r'[^\w\s\-~<>.:/@%+*#°₩$가-힣]', '', str(text))
    text = re.sub(r'[\n\r]', ' ', text)
    return text.strip().lower()

# ✅ 수정: DataFrame 컬럼에 직접 적용
df["benefit_details"] = df["benefit_details"].apply(clean_text)
df["source"] = df["source"].apply(clean_text)
df["keywords"] = df["keywords"].apply(lambda x: [clean_text(k) for k in x])


# %% [4] 나이 필터링 (음수나 비현실적 값 제거)
df["min_age"] = df["min_age"].apply(lambda x: x if 0 <= x <= 120 else 0)
df["max_age"] = df["max_age"].apply(lambda x: x if 0 <= x <= 120 else 99)

# %% [5] 날짜 필드 정제
df["start_date"] = df["start_date"].apply(normalize_date)
df["end_date"] = df["end_date"].apply(normalize_date)

# %% [6] 지역 정보 확인 (빈 문자열 대체)
df["area"] = df["area"].fillna("")
df["district"] = df["district"].fillna("")

# %% [7] 성별, 소득, 가구 유형 정제 (기본값 설정)
df["gender"] = df["gender"].replace("", "전체")
df["income_category"] = df["income_category"].replace("", "정보 없음")
df["household_category"] = df["household_category"].replace("", "해당 없음")

# %% [8] 저장
output_dir = Path("1.data")
output_dir.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = output_dir / f"{timestamp}_llm_code_processed.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"✅ 코드 기반 전처리 저장 완료: {output_file}")
