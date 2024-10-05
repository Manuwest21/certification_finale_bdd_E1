import os
import sqlite3

# Obtenir le répertoire du script actuel
repertoire_actuel = os.getcwd()

# Définir le chemin pour la base de données (dans le répertoire actuel)
chemin_bdd = os.path.join(repertoire_actuel, 'bdd_luminosite15.db')

# Connexion à la base de données SQLite
connexion = sqlite3.connect(chemin_bdd)
curseur = connexion.cursor()

# Supprimer les tables existantes si elles existent
curseur.execute("DROP TABLE IF EXISTS frequentation")
curseur.execute("DROP TABLE IF EXISTS lumiere")
curseur.execute("DROP TABLE IF EXISTS objets_trouves")

# Créer la table 'frequentation' avec nom_gare comme clé primaire
curseur.execute("""
    CREATE TABLE frequentation(
        nom_gare TEXT PRIMARY KEY NOT NULL,
        frequent_2021 INTEGER,
        frequent_2022 INTEGER,
        frequent_2023 INTEGER
    )
""")

# Créer la table 'lumiere'
curseur.execute("""
    CREATE TABLE lumiere(
        date TEXT NOT NULL PRIMARY KEY,
        cloud INTEGER,
        sun INTEGER,
        annee INTEGER 
    )
""")

# Créer la table 'objets_trouves' avec une clé étrangère pour la gare
curseur.execute("""
    CREATE TABLE objets_trouves(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        type TEXT,
        nom_gare TEXT NOT NULL,
        poids_pondere FLOAT,
        FOREIGN KEY (date) REFERENCES lumiere(date),
        FOREIGN KEY (nom_gare) REFERENCES frequentation(nom_gare)
    )
""")

# Fermer la connexion
connexion.commit()
connexion.close()

print(f"Base de données créée dans : {chemin_bdd}")

