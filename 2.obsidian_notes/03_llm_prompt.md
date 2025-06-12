# 03 LLM 프롬프트 설계 및 추론

## 📌 목표

* LLM을 활용해 정책 텍스트로부터 구조화된 JSON 정보 추출
* 후속 검색, 추천, 분류를 위한 전처리 데이터 생산

---

## \[1] 데이터 구성 및 준비

* 입력 경로: `1.data/20250608_163125_prompt_ready.csv`
* 주요 컬럼: `서비스ID`, `제목`, `본문`
* 텍스트 전처리: 개행 제거 및 소문자 통일

```python
def clean_text(text):
    if text is None:
        return ""
    text = re.sub(r'[^\w\s\-~<>.:/@%+*#°₩$]', '', text)
    text = re.sub(r'[\n\r]', ' ', text)
    return text.strip().lower()
```

---

## \[2] 프롬프트 설계

### 🧠 System Prompt

* 정책 정보를 JSON 항목으로 추출하는 역할 부여
* JSON 필드 예시: `area`, `min_age`, `max_age`, `support_type`, `application_method`, 등 총 25개 항목
* JSON 외 출력 금지 (마크다운, 설명 제거)

### 🙋‍♀️ Human Prompt

* `제목`과 `본문` 정보를 그대로 포함하여 모델에게 전달

```md
# 혜택 정보 텍스트:
제목: {title}
본문: {content}
```

---

## \[3] JSON 출력 스키마

### 🎯 추출 예시

```json
{
  "area": "전국",
  "min_age": 19,
  "max_age": 39,
  "support_type": "현금",
  "source": "복지로"
}
```

* 항목 누락 또는 형식 불일치 시 후처리에서 필터링 예정

---

## \[4] Fake LLM 테스트 함수

* 실제 LLM 사용 전 추출 포맷과 구조 점검용
* `fake_llm_response()` 함수로 구조 점검만 수행
* 정책 정보는 무작위 또는 샘플링된 값으로 채움

---

## \[5] 결과 저장

* 저장 위치: `1.data/YYYYMMDD_HHMMSS_llm_result.json`
* 저장 형식: JSON 리스트 (서비스ID 포함)

```json
[
  {
    "서비스ID": "BNF000001",
    "area": "전국",
    "min_age": 0,
    "support_type": "기타"
  }
]
```

---

## \[6] 활용 방안

* 정책 텍스트 기반 카테고리 자동 분류
* 사용자 입력 정보와 매칭해 개인화 정책 추천
* 시각화 자료 구성 및 대시보드 기초 데이터로 사용




---

## 🧾 포트폴리오 PPT에 넣을만한 요소

### 🔹 1. 시각화 자료
- **전체 파이프라인 다이어그램**:  
  `원본 CSV ➝ Prompt 생성 ➝ LLM 추론 ➝ JSON 저장 ➝ 후속 처리`
- **Prompt 예시 vs 응답 예시**:  
  좌우 비교 표 (2-column)

### 🔹 2. 기술 스택 태그 이미지
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
- ![LangChain](https://img.shields.io/badge/-LangChain-00BFFF)
- ![Gemini](https://img.shields.io/badge/-Gemini%20LLM-black)

### 🔹 3. 결과 이미지
- JSON 구조 일부 강조 (스크린샷 or 코드박스)
- 결과 3~4개 시각화된 요약표 (예: 나이/소득 조건 비교표)

### 🔹 4. 활용 가능성
- 정책 추천 엔진
- 수혜자 맞춤 필터링
- 챗봇 연계

---

요약하자면, 지금 너한테 필요한 건:
- 📁 `03-llm_prompt.md` → 위 템플릿 쓰면 됨  
- 🖼️ PPT용 시각자료 → 다이어그램, 태그, JSON 샘플


