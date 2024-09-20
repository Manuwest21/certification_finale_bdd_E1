import sqlite3
import pyodbc

# Connexion à la base de données SQLite
conn_sqlite = sqlite3.connect('bdd_luz.db')
cursor_sqlite = conn_sqlite.cursor()

# Extraire les données de la table 'lumiere'
cursor_sqlite.execute("SELECT * FROM lumiere")
data_lumiere = cursor_sqlite.fetchall()

# Extraire les données de la table 'objets_trouves'
cursor_sqlite.execute("SELECT * FROM objets_trouves")
data_objets_trouves = cursor_sqlite.fetchall()

# Fermer la connexion SQLite
conn_sqlite.close()

# Connexion à SQL Azure
conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=influ_luminosite;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

# Insertion des données dans la table 'lumiere'
for row in data_lumiere:
    cursor_azure.execute("""
        INSERT INTO lumiere (date, cloudcover, sunhour)
        VALUES (?, ?, ?)
    """, row[0], row[1], row[2])

# Commit des transactions pour la table 'lumiere'
conn_azure.commit()

# Insertion des données dans la table 'objets_trouves'
for row in data_objets_trouves:
    cursor_azure.execute("""
        INSERT INTO objets_trouves (date, type, gare)
        VALUES (?, ?, ?)
    """, row[0], row[1], row[2])

# Commit des transactions pour la table 'objets_trouves'
conn_azure.commit()

# Fermer la connexion SQL Azure
conn_azure.close()

