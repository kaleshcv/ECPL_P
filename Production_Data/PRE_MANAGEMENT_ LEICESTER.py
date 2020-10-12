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
df_sheet1=pd.read_excel('//172.16.10.12/PowerBI Reports/PRE MANAGEMENT LEICESTER LTD/PRE MANAGEMENT LEICESTER LTD.xlsx',sheet_name='Sheet1')

# First Insertion - DONE
#df_sheet1.to_sql('Pre_mgt_Leic_ltd',con=connection,if_exists='append',index=False)

#   Reeding from SQL
df_from_sql_sheet1=pd.read_sql('SELECT * FROM Pre_mgt_Leic_ltd',con=connection)

#   Finding Last index
l_sheet1=df_from_sql_sheet1.index[-1]
l_sheet1+=1
print(l_sheet1)


# Data to Database sheet1
df_new_sheet1=df_sheet1.iloc[l_sheet1:]
print(df_new_sheet1)


#print(df_new_sheet1)

# Writing to SQL
df_new_sheet1.to_sql('Pre_mgt_Leic_ltd',con=connection,if_exists='append',index=False)

#10/8/2020 - 9.00PM
