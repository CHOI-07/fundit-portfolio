# %% [1] 모듈 임포트
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from pathlib import Path
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

matplotlib.rc('font', family='Malgun Gothic')  # 한글 폰트 설정
matplotlib.rcParams['axes.unicode_minus'] = False

# %% [2] 데이터 로드_전처리된 프롬프트 입력 데이터 로드 (출처: pre_prompt.py 결과물)
df = pd.read_csv("1.data/20250608_170314_prompt_ready.csv")
df["본문"] = df["본문"].astype(str)

# %% [3] 전처리된 프롬프트 본문 길이 분포 (히스토그램)
df["본문 길이"] = df["본문"].str.len()
Path("3.images").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
sns.histplot(df["본문 길이"], bins=30, kde=True, color='steelblue')
plt.title("전처리된 프롬프트 본문 길이 분포")
plt.xlabel("문자 수")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig("3.images/2_1_pre_promptlen_distribution.png")
plt.show()

# %% [4] 전처리된 프롬프트 본문 길이 Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(y=df["본문 길이"], color='salmon')
plt.title("전처리된 프롬프트 본문 길이 Boxplot")
plt.ylabel("문자 수")
plt.tight_layout()
plt.savefig("3.images/2_2_promptlen_boxplot.png")
plt.show()

# %% [5] 전처리된 프롬프트 제목 길이 분포(문자 수 기준)
df["제목 길이"] = df["제목"].astype(str).str.len()

plt.figure(figsize=(8, 5))
sns.histplot(df["제목 길이"], bins=30, kde=True, color='mediumpurple')
plt.title("전처리된 프롬프트 제목 길이 분포")
plt.xlabel("문자 수")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig("3.images/2_3_titlelen_distribution.png")
plt.show()

# %% [6] 전처리된 프롬프트 제목 단어 수 분포
df["제목 단어 수"] = df["제목"].astype(str).apply(lambda x: len(x.split()))

plt.figure(figsize=(8, 5))
sns.histplot(df["제목 단어 수"], bins=15, kde=True, color='darkorange')
plt.title("전처리된 프롬프트 제목 단어 수 분포")
plt.xlabel("단어 수")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig("3.images/2_4_title_wordcount_dist.png")
plt.show()

# %% [7] 전처리된 프롬프트 본문 문장 수 분포 (nltk 기반)
df["문장 수"] = df["본문"].apply(lambda x: len(sent_tokenize(x)))

plt.figure(figsize=(8, 5))
sns.histplot(df["문장 수"], bins=30, kde=True, color='mediumseagreen')
plt.title("전처리된 프롬프트 본문 문장 수 분포")
plt.xlabel("문장 수")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig("3.images/2_5_prompt_sentcount_dist.png")
plt.show()


'''
실험 목적 (배경)
우리는 LLM에 **정책 데이터(본문)**를 입력하여 추론 결과(JSON)를 생성하고 있어.

그런데 LLM은 입력 길이에 따라 응답 품질과 처리 속도가 영향을 받는다.

특히, 너무 짧은 텍스트는 정보 부족, 너무 긴 텍스트는 요약/압축 오류가 날 수 있다.
'''
