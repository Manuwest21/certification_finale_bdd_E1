import sqlite3
import azure
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



import pyodbc



# Insertion des données dans la table 'lumiere'
for row in data_lumiere:
    cursor_azure.execute("""
        INSERT INTO lumiere (date, cloudcover, sunhour)
        VALUES (?, ?, ?)
    """, row[0], row[1], row[2])
    conn_azure.commit()

# Insertion des données dans la table 'objets_trouves'
for row in data_objets_trouves:
    cursor_azure.execute("""
        INSERT INTO objets_trouves (date, type, gare)
        VALUES (?, ?, ?)
    """, row[0], row[1], row[2])
    conn_azure.commit()

# Fermer la connexion SQL Azure
conn_azure.close()
