# 02_pre-prompt.md

## ✨ 목적
LLM 기반 추출을 위한 프롬프트 데이터셋 구성 단계

---

## 🔍 원본 데이터 구조
- 파일명: `20250304.csv`
- 총 컬럼 수: 22개
- 주요 내용: 정책명, 지원대상, 신청방법, 기관 정보 등

---

## 🔎 주요 처리 내용

| 단계 | 설명 |
|------|------|
| 컬럼 필터링 | 분석 목적에 따라 8개 핵심 컬럼만 추출 |
| 텍스트 정제 | 개행 문자 제거 및 앞뒤 공백 처리 |
| 프롬프트 구성 | `서비스명` → 제목 / 나머지 항목 → 본문 |
| 저장 | `2.prompt_ready/prompt_ready.csv` 경로에 저장 |

---

### 🛠️ Prompt-Ready Dataset 생성

- **목적**: LLM에게 학습 가능한 텍스트 형태로 변환
- **입력 컬럼**: `지원대상`, `지원내용`, `신청기한`, ...
- **출력 구조**: `제목`, `본문` → Gemini Prompt 입력용
- **저장 위치**: `2.prompt_ready/{timestamp}_prompt_ready.csv`
- **특징**: 시계열 버전 관리, 인코딩 utf-8-sig


## 🛠 사용 함수 정리

```python
def clean_text(text):
    return str(text).replace('\n', ' ').replace('\r', ' ').strip()

def make_prompt(row):
    ...

### 📦 데이터셋 저장 경로 및 구조
- 저장 파일명: `{타임스탬프}_prompt_ready.csv`
- 저장 경로: `2.prompt_ready/`
- 인코딩: `utf-8-sig` (Excel 호환)

```python
csv_filename = f"{timestamp}_prompt_ready.csv"
prompt_df.to_csv(csv_path, index=False, encoding="utf-8-sig")
