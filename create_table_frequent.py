import sqlite3

connexion=sqlite3.connect("bdd_luz.db")
curseur=connexion.cursor()
curseur.execute("DROP TABLE IF EXISTS frequentation")
try:
    curseur.execute("""
        CREATE TABLE frequentation (
            nom_gare TEXT NOT NULL PRIMARY KEY,
            frequent_2021 INTEGER,
            frequent_2022 INTEGER,
            frequent_2023 INTEGER
        )
    """)
    print("Table 'frequentation' créée avec succès.")
except sqlite3.Error as e:
    print("Erreur lors de la création de la table :", e)
connexion.commit()
connexion.close()