import pandas as pd
from sqlalchemy import create_engine
SERVER='172.16.10.15'
DATABASE='sampleDB'
DRIVER='SQL Server Native Client 11.0'
USERNAME='sa'
PASSWORD='@cct3@m'
DATABASE_CONNECTION=f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'


engine=create_engine(DATABASE_CONNECTION)
connection=engine.connect()
data=pd.read_sql_query('select * from aadya',connection)
print(data)



