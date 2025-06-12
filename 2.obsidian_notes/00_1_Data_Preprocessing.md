## 실험 목적
- 로우 데이터를 분석하여 LLM 입력에 필요한 유효 컬럼을 판단하기 위한 기초 전처리

## 실험 방법
- `20250304.csv` 기준 컬럼별 결측치 비율 계산 (`.isnull().mean()`)
- 시각화 파일: `1.1_rowdata_null_ratio.py` → `3.images/1.1_rowdata_null_ratio.png`

## 결과 요약
- `접수기관`, `선정기준` 컬럼은 각각 약 91%, 90%의 결측치를 가짐
- 해당 컬럼은 이후 LLM 입력 프롬프트 생성에서 제외하기로 결정
- 이 외 대부분의 주요 텍스트 필드는 결측치가 거의 없음

![[3.images/1.1_rowdata_null_ratio.png]]
"C:\Users\hhhey\Desktop\ME\1.re_project\Fundit-Project\3.images\1.1_rowdata_null_ratio.png"