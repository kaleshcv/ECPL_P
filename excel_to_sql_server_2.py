import pandas as pd
from sqlalchemy import create_engine
#credentials

SERVER='172.16.10.15'
DATABASE='sampleDB'
DRIVER='SQL Server Native Client 11.0'
USERNAME='sa'
PASSWORD='@cct3@m'

#Connection
DATABASE_CONNECTION=f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine=create_engine(DATABASE_CONNECTION)
connection=engine.connect()

#Reading Excel
df=pd.read_excel('AADYA _SOLUTIONS.xlsx')
#Reading old csv
df_old=pd.read_csv('AADYA_OLD.csv')


#Writing to SQL
#df.to_sql('AADYA_NEW_PY',con=connection,if_exists='append',index=True)
#df.to_sql('AADYA_NEW_PY',con=connection,if_exists='replace',index=True)
print('Done')
#df.to_csv('AADYA_OLD.csv')
