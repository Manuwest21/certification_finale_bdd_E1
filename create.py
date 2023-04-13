import sqlite3

connexion=sqlite3.connect("bddt.db")
curseur=connexion.cursor()

curseur.execute("DROP TABLE IF EXISTS gare")
curseur.execute(""" CREATE TABLE  gare(
                    nom_gare TEXT NOT NULL PRIMARY KEY,
                    frequent_2019 INTEGER,
                    frequent_2020 INTEGER,
                    frequent_2021 INTEGER,
                    frequent_2022 INTEGER
                )
                """)

connexion.commit()

curseur.execute(""" CREATE TABLE IF NOT EXISTS meteo(
                    date TEXT NOT NULL PRIMARY KEY,
                    temperature INTEGER
                   
                )
                """)

connexion.commit()

curseur.execute(""" CREATE TABLE IF NOT EXISTS obj_semaine(
                    week TEXT NOT NULL PRIMARY KEY,
                    obj_trouves INTEGER
                   
                )
                """)

connexion.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS objets_trouves(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    typo TEXT NOT NULL,
                    gare TEXT NOT NULL,
                    nom_gare TEXT NULL,
                    date_meteo TEXT NULL,
                    FOREIGN KEY (nom_gare) REFERENCES gare(nom_gare),
                    FOREIGN KEY (date_meteo) REFERENCES meteo(date)
                )
                """)

connexion.commit()
connexion.close()
