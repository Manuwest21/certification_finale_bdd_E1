import pandas as pd
import sqlite3


df= pd.read_csv("concat.csv")
daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
daf.rename(columns={"fields.date":"data"},inplace=True)
daf.rename(columns={"fields.gc_obo_type_c":"typo"},inplace=True)
daf.rename(columns={"fields.gc_obo_gare_origine_r_name":"gare"},inplace=True)
daf['date'] = daf['date'].str.slice(stop=10)

daf = daf[['data', 'typo', 'gare']]
daf['data']=daf['data'].apply(lambda x : x[:10])

df = pd.read_csv('temp_paris.csv')
dif = pd.read_csv('frequentation.csv')

conn = sqlite3.connect('bdd.db')
curseur = conn.cursor()

for index, row in df.iterrows():
    curseur.execute("INSERT INTO meteo (date, temperature) VALUES (?, ?)", (row['date'], row['temperature_moyenne_°C']))
conn.commit()   
for index, row in dif.iterrows():
    curseur.execute("INSERT INTO gare (nom_gare, frequent_2019,frequent_2020,frequent_2021,frequent_2022) VALUES (?, ?,?,?,?)", (row['gare'], row['frequent_2019'],row['frequent_2020'],row['frequent_2021'],row['frequent_2022']))
conn.commit()    

for index, row in daf.iterrows():
    curseur.execute("INSERT INTO objets_trouves (data,typo,gare) VALUES (?, ?,?)", (row['data'], row['typo'],row['gare']))
conn.commit()    
conn.close()


