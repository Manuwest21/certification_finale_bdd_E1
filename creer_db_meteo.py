import pandas as pd
import sqlite3

# Chargement des données CSV dans un DataFrame pandas
df = pd.read_csv('temp_paris.csv')

# Connexion à la base de données SQLite
conn = sqlite3.connect('bdd1.db')

# Écriture du DataFrame dans une table SQL
df.to_sql('meteo', conn, if_exists='replace', index=False)

# Fermeture de la connexion
conn.close()
