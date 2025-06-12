# 2.1 LLM 응답 결과 분석

## 📌 목적

`2_0_llm_prompt_generation.py`를 통해 생성된 LLM 응답(JSON)을 기반으로, 응답 필드의 품질과 구성을 진단한다. 이는 아래와 같은 분석 목적을 달성하기 위함이다:

* LLM의 응답 구조가 일관되게 출력되고 있는가?
* 특정 필드에서 요약이 잘 적용되었는가?
* default 값만 반복되는 필드는 어떤 것이 있는가?
* 이후 fine-tuning, 후처리 룰 개선, RAG retrieval 키워드 생성 등에 활용 가능한가?

분석 결과를 통해, RAG 입력 품질을 사전 진단하고 구조상 한계를 명확히 파악할 수 있다.

## 📊 주요 분석 항목

### 1. `benefit_details` 길이 분포

* 대부분 응답이 **100자 이하로 압축**되어 있음
* 이는 모델 출력 제한 혹은 프롬프트 길이 제약 조건이 잘 적용되었음을 의미함
* → **요약 응답 품질 양호함**
* !\[\[3.images/2\_1\_benefit\_details\_len\_dist.png]]

### 2. `keywords` 키워드 개수 분포

* 대부분의 응답은 **2\~3개의 키워드**로 구성되어 있음
* 일부 1개만 존재하는 응답도 존재 → 입력 제목의 길이 영향 가능성 있음
* → **프롬프트 title 기반 키워드 분리 품질 진단 가능**
* !\[\[3.images/2\_2\_keyword\_count\_dist.png]]

### 3. `support_type`, `benefit_category`, `application_method`

* 전 응답이 동일한 값으로 구성됨:

  * `support_type`: 기타
  * `benefit_category`: 생활안정
  * `application_method`: 온라인 신청
* → 실제 분류 기능이 작동하지 않았거나, 입력 부족으로 default 응답만 제공된 상황
* !\[\[3.images/2\_3\_support\_type\_dist.png]]
* !\[\[3.images/2\_4\_benefit\_category\_dist.png]]
* !\[\[3.images/2\_5\_application\_method\_dist.png]]

## 🔍 정리 및 인사이트

* ✅ `benefit_details`, `keywords`는 **입력 → 출력** 구조상 품질 진단이 가능하고 시각화 유지 가치 있음
* ⚠️ `support_type`, `benefit_category`, `application_method`는 **값이 단일(default)로 응답**되므로 분포 정보로써 의미는 낮음
* ❌ `min_age`, `max_age` 등은 전부 고정값이거나 비어있어 **시각화 제거**

## 📁 참고

* 입력 데이터: `2.llm_result/20250612_140851_llm_result.csv`
* 분석 스크립트: `2_1_LLM_Response_Analysis.py`
* 생성 이미지: `3.images/2_1~2_6_*.png`
