import pandas as pd
from sqlalchemy import create_engine

#   credentials
SERVER='172.16.10.15'
DATABASE='ProductionDB'
DRIVER='SQL Server Native Client 11.0'
USERNAME='sa'
PASSWORD='@cct3@m'

#   Connection
DATABASE_CONNECTION=f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine=create_engine(DATABASE_CONNECTION)
connection=engine.connect()

#   Reading Excel
df_sheet1=pd.read_excel('//172.16.10.12/PowerBI Reports/SUCCESS SYSTEMS/Sucess Systems PBI.xlsx',sheet_name='Raw Data')
#df_sheet1=df_sheet1.dropna()


# First Insertion - Done
#df_sheet1.to_sql('success_systems',con=connection,if_exists='append',index=False)

#   Reeding from SQL
df_from_sql_sheet1=pd.read_sql('SELECT * FROM success_systems',con=connection)
#print(df_from_sql_sheet1)


#   Finding Last index
l_sheet1=df_from_sql_sheet1.index[-1]
l_sheet1+=1
#print(l_sheet1)


# Data to Database sheet1
df_new_sheet1=df_sheet1.iloc[l_sheet1:]

print(df_new_sheet1)

# Writing to SQL

#df_new_sheet1.to_sql('success_systems',con=connection,if_exists='append',index=False)


#10/6/2020
