#%%
import pandas as pd

df = pd.read_csv('1.data/20250304.csv')
print(df.info())


# %%
print(df.head())
# %%
print(df.isnull().sum())

# %%
