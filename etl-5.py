import sqlalchemy as sql
import pandas as pd

conn_string="mysql+pymysql://root:@localhost/bigdata6"
sql_engine=sql.create_engine(conn_string)

ds=pd.read_csv("pegawai_cab01.csv")
df=ds[['job_id','job_title']].drop_duplicates()

df.to_sql("job",con=sql_engine,if_exists='replace',index=False)
