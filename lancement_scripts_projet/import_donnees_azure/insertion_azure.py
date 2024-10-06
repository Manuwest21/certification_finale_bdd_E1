import os
import sqlite3
import pyodbc

# Obtenir le répertoire actuel
repertoire_actuel = os.getcwd()

# Construire le chemin vers la base de données dans le répertoire parent et 'nettoyage_des_donnees'
chemin_bdd = os.path.join(repertoire_actuel, '../nettoyage_des_donnees/bdd_pondere.db')

# Résoudre le chemin absolu au cas où il y aurait des liens symboliques ou des chemins relatifs
chemin_bdd = os.path.abspath(chemin_bdd)

# Connexion à la base de données SQLite
conn_sqlite = sqlite3.connect(chemin_bdd)
cursor_sqlite = conn_sqlite.cursor()

print(f"Connexion réussie à la base de données SQLite à l'emplacement : {chemin_bdd}")

# Connexion à la base de données Azure SQL via pyodbc
conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

print("Connexion réussie à la base de données Azure.")




# --- Extraire les données des tables locales ---

# Extraire les données de la table 'lumiere' depuis bdd_pondere.db
cursor_sqlite.execute("SELECT * FROM lumiere")
lumiere_data = cursor_sqlite.fetchall()

# Extraire les données de la table 'frequentation' depuis bdd_pondere.db
cursor_sqlite.execute("SELECT * FROM frequentation")
frequentation_data = cursor_sqlite.fetchall()

# Extraire les données de la table 'objets_trouves' depuis bdd_pondere.db
cursor_sqlite.execute("SELECT * FROM objets_trouves")
objets_data = cursor_sqlite.fetchall()

# --- Insertion des données dans les tables Azure ---

# Insérer les données dans la table 'lumiere1' d'Azure
for row in lumiere_data:
    cursor_azure.execute("INSERT INTO lumiere1 (date, cloud, sun) VALUES (?, ?, ?)", row[:3])
print("import luz ok")
# Insérer les données dans la table 'frequentation1' d'Azure
for row in frequentation_data:
    cursor_azure.execute("INSERT INTO frequentation1 (gare, frequent_2021, frequent_2022, frequent_2023) VALUES (?, ?, ?, ?)", row[:4])
print("import frequentation ok")
# Insérer les données dans la table 'objets_trouves1' d'Azure
n=1
for row in objets_data:
    cursor_azure.execute("INSERT INTO objets_trouves1 (date, type, gare, poids_pondere) VALUES (?, ?, ?, ?)", row[1:5])
    print(n)
    n=n+1
# Commit les transactions sur Azure
conn_azure.commit()

# --- Fermer les connexions ---
conn_sqlite.close()
conn_azure.close()

print("Données insérées avec succès dans la base de données Azure.")