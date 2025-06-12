#$$
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

matplotlib.rc('font', family='Malgun Gothic')  # 한글 폰트 설정 (Windows)
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 1번 스크립트 실행 후 저장된 원본 전처리 파일
INPUT_PATH = Path("1.data/20250304.csv")
df = pd.read_csv(INPUT_PATH)
#%%
# 결측치 비율 시각화
null_ratio = df.isnull().mean().sort_values(ascending=False) * 100


#%%

plt.figure(figsize=(10, 6))
null_ratio.plot(kind='bar', color='skyblue')
plt.title("전처리 전 컬럼별 결측치 비율 (%)")
plt.ylabel("결측치 비율 (%)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("3.images/0_1_rowdata_null_ratio.png")  # ← 캡처 저장
plt.show()
