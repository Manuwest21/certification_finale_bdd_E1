import sqlite3

connexion=sqlite3.connect("bdd1.db")
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

curseur.execute(""" CREATE TABLE IF NOT EXISTS meteo(
                    date TEXT NOT NULL PRIMARY KEY,
                    temperature INTEGER
                   
                )
                """)

connexion.commit()
