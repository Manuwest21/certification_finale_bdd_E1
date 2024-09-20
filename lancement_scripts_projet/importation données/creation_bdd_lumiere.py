import sqlite3
import os

# Obtenir le répertoire du script
repertoire_script = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin complet pour la base de données
# Aller un niveau au-dessus du répertoire du script et entrer dans le dossier 'nettoyage_des_donnees'
chemin_bdd = os.path.join(repertoire_script, '..', 'importation données', 'bdd_luminosite.db')

# S'assurer que le répertoire 'nettoyage_des_donnees' existe
os.makedirs(os.path.dirname(chemin_bdd), exist_ok=True)

# Créer une connexion à la base de données (elle sera créée dans le répertoire 'nettoyage_des_donnees')
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
        sun INTEGER
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

# Valider les changements et fermer la connexion
connexion.commit()
connexion.close()

print(f"La base de données a été créée avec succès dans le répertoire : {os.path.dirname(chemin_bdd)}")
