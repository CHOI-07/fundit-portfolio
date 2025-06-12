
#%%
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import ast

matplotlib.rc('font', family='Malgun Gothic') 
matplotlib.rcParams['axes.unicode_minus'] = False  

INPUT_PATH = Path("2.llm_result/20250612_140851_llm_result.csv")
df = pd.read_csv(INPUT_PATH)

# %% [2] 데이터 로드
df = pd.read_csv("2.llm_result/20250612_140851_llm_result.csv")
df["benefit_details"] = df["benefit_details"].astype(str)
df["keywords"] = df["keywords"].astype(str)

Path("3.images").mkdir(parents=True, exist_ok=True)

# %% [3] benefit_details 길이 분포
df["benefit_len"] = df["benefit_details"].str.len()

plt.figure(figsize=(8, 5))
sns.histplot(df["benefit_len"], bins=30, kde=True, color="steelblue")
plt.title("benefit_details 길이 분포")
plt.xlabel("문자 수")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig("3.images/2_1_benefit_details_len_dist.png")
plt.close()

# %% [4] keywords 개수 분포
df["keyword_count"] = df["keywords"].apply(lambda x: len(ast.literal_eval(x)) if pd.notnull(x) else 0)

plt.figure(figsize=(8, 5))
sns.histplot(df["keyword_count"], bins=15, kde=False, color="orange")
plt.title("키워드 개수 분포")
plt.xlabel("키워드 수")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig("3.images/2_2_keyword_count_dist.png")
plt.close()

# %% [5] 지원 유형 분포
plt.figure(figsize=(8, 5))
df["support_type"].value_counts().plot(kind="bar", color="skyblue")
plt.title("지원 유형 (support_type) 분포")
plt.xlabel("유형")
plt.ylabel("빈도")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("3.images/2_3_support_type_dist.png")
plt.close()

# %% [6] 혜택 카테고리 분포
plt.figure(figsize=(8, 5))
df["benefit_category"].value_counts().plot(kind="bar", color="seagreen")
plt.title("혜택 카테고리 분포")
plt.xlabel("카테고리")
plt.ylabel("빈도")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("3.images/2_4_benefit_category_dist.png")
plt.close()

# %% [7] 신청 방식 분포
plt.figure(figsize=(8, 5))
df["application_method"].value_counts().plot(kind="bar", color="purple")
plt.title("신청 방식 분포")
plt.xlabel("방식")
plt.ylabel("빈도")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("3.images/2_5_application_method_dist.png")
plt.close()

# %% [8] 나이 조건 분포
plt.figure(figsize=(8, 5))
sns.histplot(df["min_age"], bins=30, color="salmon", label="min_age", kde=False, alpha=0.6)
sns.histplot(df["max_age"], bins=30, color="navy", label="max_age", kde=False, alpha=0.6)
plt.title("나이 조건 분포 (min_age vs max_age)")
plt.xlabel("나이")
plt.ylabel("빈도")
plt.legend()
plt.tight_layout()
plt.savefig("3.images/2_6_age_condition_dist.png")
plt.close()
