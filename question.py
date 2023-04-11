import pandas as pd



df= pd.read_csv("concat.csv")
daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
daf.rename(columns={"fields.date":"date"},inplace=True)
daf.rename(columns={"fields.gc_obo_type_c":"type"},inplace=True)
daf.rename(columns={"fields.gc_obo_gare_origine_r_name":"nom_gare"},inplace=True)
# daf['date'] = daf['date'].str.slice(stop=10)
# daf['date']=daf['date'].apply(lambda x : x [:10])
daf['date'] = pd.to_datetime(daf['date'])

