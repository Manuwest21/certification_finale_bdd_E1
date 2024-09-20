import sqlite3
import pyodbc
# Connexion à la base de données SQLite
conn_sqlite = sqlite3.connect('bdd_pondere.db')
cursor_sqlite = conn_sqlite.cursor()

# Extraire les données de la table 'lumiere'
cursor_sqlite.execute("SELECT * FROM frequentation")
data_frequentation = cursor_sqlite.fetchall()

# # Extraire les données de la table 'objets_trouves'
# cursor_sqlite.execute("SELECT * FROM objets_trouves")
# data_objets_trouves = cursor_sqlite.fetchall()

# Fermer la connexion SQLite
conn_sqlite.close()

# Connexion à SQL Azure
conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()




# --- Extraire les données des tables locales ---

# Extraire les données de la table 'lumiere' depuis bdd_pondere.db
curseur_sqlite.execute("SELECT * FROM lumiere")
lumiere_data = curseur_sqlite.fetchall()

# Extraire les données de la table 'frequentation' depuis bdd_pondere.db
curseur_sqlite.execute("SELECT * FROM frequentation")
frequentation_data = curseur_sqlite.fetchall()

# Extraire les données de la table 'objets_trouves' depuis bdd_pondere.db
curseur_sqlite.execute("SELECT * FROM objets_trouves")
objets_data = curseur_sqlite.fetchall()

# --- Insertion des données dans les tables Azure ---

# Insérer les données dans la table 'lumiere9' d'Azure
for row in lumiere_data:
    cursor_azure.execute("INSERT INTO lumiere9 (date, cloud, sun) VALUES (?, ?, ?)", row)

# Insérer les données dans la table 'frequentation9' d'Azure
for row in frequentation_data:
    cursor_azure.execute("INSERT INTO frequentation9 (gare, frequent_2021, frequent_2022, frequent_2023) VALUES (?, ?, ?, ?)", row[1:])

# Insérer les données dans la table 'objets_trouves9' d'Azure
for row in objets_data:
    cursor_azure.execute("INSERT INTO objets_trouves9 (date, type, gare, poids_pondere) VALUES (?, ?, ?, ?)", row[1:])

# Commit les transactions sur Azure
conn_azure.commit()

# --- Fermer les connexions ---
conn_sqlite.close()
conn_azure.close()

print("Données insérées avec succès dans la base de données Azure.")