import sqlite3
import os

# Obtenir le répertoire du script
repertoire_script = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin complet pour la base de données
chemin_bdd = os.path.join(repertoire_script, "bdd_objets_luminosite.db")

# Créer une connexion à la base de données (elle sera créée dans le répertoire du script)
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
        annee INTEGER NOT NULL
    )
""")

# Créer la table 'objets_trouves' avec une clé étrangère pour la gare
curseur.execute("""
    CREATE TABLE objets_trouves(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT,
        nom_gare TEXT NOT NULL,
        FOREIGN KEY (date) REFERENCES lumiere(date),
        FOREIGN KEY (nom_gare) REFERENCES frequentation(nom_gare)
    )
""")

connexion.commit()
connexion.close()