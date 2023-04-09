import pandas as pd
import sqlite3

# Chargement des données CSV dans un DataFrame pandas
df = pd.read_csv('temp_paris.csv')
dif = pd.read_csv('frequentation.csv')
# Connexion à la base de données SQLite
conn = sqlite3.connect('bddt.db')

# Écriture du DataFrame dans une table SQL
# df.to_sql('meteo', conn, if_exists='replace', index=False)

# Fermeture de la connexion


curseur = conn.cursor()

for index, row in df.iterrows():
    curseur.execute("INSERT INTO meteo (date, temperature) VALUES (?, ?)", (row['date'], row['temperature_moyenne_°C']))
for index, row in dif.iterrows():
    curseur.execute("INSERT INTO gare (nom_gare, frequent_2019,frequent_2020,frequent_2021,frequent_2022) VALUES (?, ?,?,?,?)", (row['gare'], row['frequent_2019'],row['frequent_2020'],row['frequent_2021'],row['frequent_2022']))
conn.commit()    
conn.close()
# # Connexion à la base de données SQLite
# conn = sqlite3.connect('bddb.db')

# # Écriture du DataFrame dans une table SQL
# dif.to_sql('gare', conn, if_exists='replace', index=False)

# # Fermeture de la connexion
# conn.close()

