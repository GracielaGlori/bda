import pandas as pd
df_csv=pd.read_csv("pegawai_cab01.csv")

df_csv_filter=df_csv[['nik','nama','job_id']]
print(df_csv_filter)