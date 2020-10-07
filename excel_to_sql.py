import pandas as pd
from sqlalchemy import create_engine
import pyodbc
pyodbc.dataSources()

df=pd.read_excel('data.xlsx')
engine=create_engine('mssql+pyodbc://sa:@cct3@m/172.16.10.15/sampleDB')
df.to_sql('new_table',con=engine,if_exists='append',index=False)
