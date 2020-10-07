import pandas as pd
from sqlalchemy import create_engine

#   credentials
SERVER='172.16.10.15'
DATABASE='sampleDB'
DRIVER='SQL Server Native Client 11.0'
USERNAME='sa'
PASSWORD='@cct3@m'

#   Connection
DATABASE_CONNECTION=f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine=create_engine(DATABASE_CONNECTION)
connection=engine.connect()

#   Reading Excel
df_sheet1=pd.read_excel('data.xlsx',sheet_name='Sheet1')


#   Sorting
#df_sheet1=df_sheet1.sort_values(by=['P_key'])

df_sheet1=df_sheet1.dropna()


# First Insertion
# df_sheet1.to_sql('sheet1',con=connection,if_exists='append',index=False)
# df_sheet2.to_sql('sheet2',con=connection,if_exists='append',index=False)


#   Reeding from SQL
df_from_sql_sheet1=pd.read_sql('SELECT * FROM sheet1',con=connection)

#df_from_sql.sort_values(by=['P_key'])

##print(df_from_sql)

#   Finding Last index
l_sheet1=df_from_sql_sheet1.index[-1]
l_sheet1+=1

# Data to Database sheet1
df_new_sheet1=df_sheet1.iloc[l_sheet1:]
df_new_sheet1=df_new_sheet1.dropna()
print(df_new_sheet1)

# Writing to SQL
df_new_sheet1.to_sql('sheet1',con=connection,if_exists='append',index=False)


