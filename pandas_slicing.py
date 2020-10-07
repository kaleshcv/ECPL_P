import pandas as pd

df=pd.read_excel('data_pandas.xlsx')

l=df.index[-1]
l+=1

df_new=df.iloc[l:]






