import sqlalchemy as sql
import pandas as pd

conn_string="mysql+pymysql://root:@localhost/bigdata6"
sql_engine=sql.create_engine(conn_string)

df_csv=pd.read_csv("pegawai_cab01.csv")
df_csv_filter=df_csv[['nik','nama','job_id']]

df_excel=pd.read_excel("pegawai_cab02.xlsx")
df_excel_filter=df_excel[df_excel['status']!='OUT']
df_excel_filter=df_excel_filter[['nik','nama','job']]
df_excel_filter=df_excel_filter.rename(columns={'job':'job_id'})

df_gabung=df_csv_filter._append(df_excel_filter,"index=False")

df_gabung.to_sql("pegawai",con=sql_engine,
                 if_exists='replace',index=False)
print("Load ke MySQL selesai")