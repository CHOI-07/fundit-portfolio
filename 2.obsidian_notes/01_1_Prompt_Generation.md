# 2.1 전처리된 프롬프트 입력 특성 분석

## 📌 목적
`pre_prompt.py`를 통해 생성된 전처리된 프롬프트 입력 데이터를 기반으로,  
LLM에 입력되는 텍스트의 **길이, 문장 수, 복잡도**를 분석한다.  
이 분석은 모델의 토큰 한계, 요약 필요성, 입력 품질을 사전에 진단하기 위함이다.

---

## 📊 분석 항목 및 시각화

### 1. 본문 길이 분포 (문자 수 기준)
- 대부분 **200~800자** 사이에 분포
- 일부는 **1500자 이상**의 long-tail 분포 → LLM 토큰 한계 초과 위험
- ![[3.images/1_1_pre_promptlen_distribution.png]]

---

### 2. 본문 길이 Boxplot
- 중앙값 약 **300자**, 일부 **3000자 이상** 이상치 존재  
- 극단적으로 긴 입력은 요약 또는 필터링 대상
- ![[3.images/1_1_promptlen_boxplot.png]]

---

### 3. 제목 길이 분포 (문자 수 기준)
- 평균 **10~20자**, 일부 **50자 초과** 존재
- 시스템 메시지 영역 침범 우려 → 압축 대상 여부 판단 가능
- ![[3.images/1_3_titlelen_distribution.png]]

---

### 4. 제목 단어 수 분포
- 평균 **2~4단어**, 일부는 **7단어 이상**
- 복잡한 제목은 분리 또는 키워드 요약 대상
- ![[3.images/1_4_title_wordcount_dist.png]]

---

### 5. 본문 문장 수 분포 (nltk 기반 문장 분리)
- 대부분 **1~4문장**, 일부 **10문장 이상** 존재
- 문장 수가 많을수록 요약 성능 저하 가능 → 제한 필요성 존재
- ![[3.images/1_5_prompt_sentcount_dist.png]]

---

## ✅ 분석 요약 및 의사결정

- **1500자 이상**, **10문장 이상** → 사전 요약 필터링 대상
- 제목이 길거나 복잡할 경우 → 시스템 메시지 침범 및 추론 성능 저하 우려
- 추론 속도, 비용 최적화를 위해 **사전 길이 진단 → 압축 전략 적용** 필요

---

## 📁 참고 자료
- 입력 데이터: `1.data/20250608_170314_prompt_ready.csv`
- 분석 스크립트: `2.1_graph_promptlen_stats.py`
- 이미지 캡처:
  - `3.images/1_1_pre_promptlen_distribution.png`
  - `3.images/1_1_promptlen_boxplot.png`
  - `3.images/1_3_titlelen_distribution.png`
  - `3.images/1_4_title_wordcount_dist.png`
  - `3.images/1_5_prompt_sentcount_dist.png`
