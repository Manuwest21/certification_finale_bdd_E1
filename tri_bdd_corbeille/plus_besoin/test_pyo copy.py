import sqlite3
import pyodbc
# Connexion à la base de données SQLite
conn_sqlite = sqlite3.connect('bdd_luz.db')
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


cursor_azure.execute(""" 
       CREATE TABLE frequentation(
            gare VARCHAR(40) PRIMARY KEY ,
            frequent_2021 INTEGER NOT NULL,
            frequent_2022 INTEGER NOT NULL,
            frequent_2023 INTEGER NOT NULL,
            )
            """)

for row in data_frequentation:
    cursor_azure.execute("""
        INSERT INTO frequentation (gare, frequent_2021, frequent_2022, frequent_2023)
        VALUES (?, ?, ?,?)
    """, row[0], row[1], row[2],row[3])


conn_azure.commit()

# Fermer la connexion SQL Azure
conn_azure.close()