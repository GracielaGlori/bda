import pandas as pd
df_excel=pd.read_excel("pegawai_cab02.xlsx")
df_excel_filter=df_excel[df_excel['status']!='OUT']
df_excel_filter=df_excel_filter[['nik','nama','job']]
df_excel_filter=df_excel_filter.rename(columns={'job':'job_id'})
print(df_excel_filter)