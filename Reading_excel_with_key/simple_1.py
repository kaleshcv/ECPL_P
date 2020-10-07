import pandas as pd

df=pd.read_excel('simple.xlsx',sheet_name='Sheet1')
df=df.dropna()
print(df)

