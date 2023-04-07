import sqlite3

connexion=sqlite3.connect("bdd2.db")
curseur=connexion.cursor()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS objets_trouves(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    typo TEXT NOT NULL,
                    nom_gare TEXT NOT NULL
                  
                    
                )
                """)




connexion.commit()


curseur.execute(""" CREATE TABLE IF NOT EXISTS gare(
                    nom_gare TEXT NOT NULL PRIMARY KEY,
                    frequent_2019 INTEGER,
                    frequent_2020 INTEGER,
                    frequent_2021 INTEGER
                )
                """)

connexion.commit()
