import pandas as pd
import sqlite3


df= pd.read_csv("fichier_concat_good_actu.csv")

n=1
conn = sqlite3.connect('bdd_luz.db')
curseur = conn.cursor()
print("1")
for index, row in df.iterrows():
    curseur.execute("INSERT INTO lumiere (date, cloud,sun) VALUES (?, ?,?)", (row['DATE'], row['CLOUDCOVER_AVG_PERCENT'], row['SUNHOUR']))
    print(n)
    n=n+1
# conn.commit()   
# for index, row in dif.iterrows():
#     curseur.execute("INSERT INTO gare (nom_gare, frequent_2019,frequent_2020,frequent_2021,frequent_2022) VALUES (?, ?,?,?,?)", (row['gare'], row['frequent_2019'],row['frequent_2020'],row['frequent_2021'],row['frequent_2022']))
# conn.commit()    

# for index, row in daf.iterrows():
#     curseur.execute("INSERT INTO objets_trouves (data,typo,gare) VALUES (?, ?,?)", (row['data'], row['typo'],row['gare']))

conn.commit()    
conn.close()