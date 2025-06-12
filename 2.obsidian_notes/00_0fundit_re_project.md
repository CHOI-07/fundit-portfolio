# 00_Fundit 프로젝트 개요 및 진행 순서

## 🎯 프로젝트 목적

* 정책/공공 혜택 데이터를 수집하고 LLM 기반으로 구조화
* 사용자 맞춤형 추천 및 시각화를 위한 기반 데이터 구축

---

## 🧭 프로젝트 전체 구조

```text
├── 00.fundit_re_project.md        <- 프로젝트 개요 및 로드맵 (요 파일)
├── 0.ori_data_preprocessing.py    <- 원본 CSV EDA 및 필터링
├── 1.llm_data_preprocessing.py    <- 프롬프트 입력 전용 데이터셋 구성
├── 2.llm_prompt_generation.py     <- Gemini 기반 JSON 추론
├── 3.llm_result_postprocess.py    <- LLM 결과 후처리 및 전처리 데이터 생성
├── 1.data/                         <- 데이터 입력/출력 디렉토리
└── 2.obsidian_notes/              <- 문서화 및 요약용 MD 파일 모음
```

---

## 🧩 단계별 요약

### \[0] 데이터 EDA 및 정제

* 정책 원본 데이터(`csv`)에서 사용할 컬럼 선별
* 중복, 누락, 불필요 컬럼 제거 → 분석/프롬프트 대상만 추출

### \[1] 프롬프트 전용 데이터 구성

* `서비스ID`, `서비스명`, `지원내용`, `지원대상` 등 주요 정보만 정제
* 텍스트 구조화 (프롬프트용 형식)

### \[2] LLM 프롬프트 설계 및 추론

* Gemini (Google Generative AI) API 사용
* 항목별 정책 JSON으로 응답 유도
* 오류 방지를 위한 system prompt 명시적 설계

### \[3] 추론 결과 후처리

* 결과 JSON 파싱 및 정규화
* `지역`, `나이`, `가구유형` 등 필드화 → DataFrame 변환

### \[4] 활용 방안

* 정책 추천 시스템 구축 가능성 탐색
* 행정구역, 대상군 별 분포 시각화 준비
* LLM 기반 질의응답 / 챗봇 구축 가능

---

## 📁 산출물

* 구조화된 정책 JSON 리스트 (`.json`)
* 후처리된 전처리 데이터셋 (`.csv`)
* Obsidian 기반 기술 문서 (`.md`)

---

## ✅ 다음 단계

* 구조화 JSON 품질 점검
* 사용자 프로파일 기반 추천 시나리오 설계
* 행정 구역 및 혜택 범주 시각화 진행

# 00\_Fundit 그룹 프로젝트 개요 및 진행 순서

## ✨ 프로젝트 개요

* 공공 정책 정보(비정형 텍스트 기반)를 구조화하여 LLM 기반 검색/추천에 활용
* 정책의 신청 자격, 대상, 조건 등을 정형화해 사용자의 조건 기반 필터링과 검색 최적화
* 전체 과정은 전처리 → LLM 추론 → 후처리 순으로 구성됨

---

## ✅ 전체 파이프라인 흐름

```
[0. 원본 CSV] → [1. 프롬프트 전처리] → [2. LLM 구조화 추론] → [3. 코드 전처리] → [4. 후속 LLM 보완 추론]
```

---

## \[0] 원본 데이터 확인

* `.csv` 형식의 공공 복지/정책 데이터
* `서비스명`, `지원내용`, `신청기한` 등 다양한 비정형 텍스트 포함
* 정책마다 형식이 달라 LLM 추론 전 구조화 필요성 확인됨

---

## \[1] pre\_prompt.py: 프롬프트 전처리

* LLM에 입력할 수 있도록 정책 텍스트를 구조화된 형태로 가공
* 주요 컬럼 필터링 + 정제(clean\_text)
* 프롬프트 형태로 title + 본문(text block) 구성

```python
def make_prompt(row):
    title = clean_text(row["서비스명"])
    content = "\n".join(
        f"{col}: {clean_text(row.get(col, ''))}"
        for col in ["등록일시", "지원대상", "지원내용", "신청기한", "신청방법"]
    )
    return {
        "서비스ID": row["서비스ID"],
        "제목": title,
        "본문": content
    }
```

* 결과물: `1.data/YYYYMMDD_prompt_ready.csv`

---

## \[2] llm\_prompt\_generation.py: LLM 추론

* Gemini 1.5 Flash를 사용하여 프롬프트 입력 → JSON 항목 구조로 출력
* System Prompt: 총 25개 항목에 대한 형식 정의
* Human Prompt: 실제 정책의 제목 및 본문 삽입
* 결과물: `1.data/YYYYMMDD_llm_result.json`

---

## \[3] 코드 기반 전처리

* LLM 없이 규칙 기반으로 정제 가능한 항목 처리:

  * `area`, `district`, `start_date`, `end_date`, `gender` 등
* 정규표현식 + 사전 정의된 행정 구역/날짜 패턴 활용
* 결과물: `processed_areaXXXX_districtXXXX.csv`

---

## \[4] 2차 LLM 보완 추론

* 코드로는 파싱이 어려운 항목:

  * `income_summary`, `personal_summary`, `keywords`, `benefit_details` 등
* 1차 결과에서 누락된 값만 필터링하여 재입력
* 실제 사용자 시나리오 기반 피드백으로 prompt 개선도 예정

---

## 📌 다음 단계 예고

* \[5] Obsidian 기반 마크다운 문서 정리 (완료)
* \[6] PPT 포트폴리오용 슬라이드 구성
* \[7] 시각화 및 검색 UI 프로토타입 구상 여부 판단

---

## 🌍 활용 가능성 및 확장

* 다양한 LLM 기반 행정 정보 구조화에 확장 가능
* 정형 DB 전환 및 정보 검색 추천, 챗봇, 통계 대시보드에 연결 가능
* 향후 API 제공 형태 또는 지역 커스터마이징 모듈 개발 여지도 존재
