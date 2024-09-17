import sqlite3

connexion=sqlite3.connect("bdd_luz_actu3.db")
curseur=connexion.cursor()

curseur.execute("DROP TABLE IF EXISTS frequentation")
curseur.execute(""" CREATE TABLE  frequentation(
                    nom_gare TEXT NOT NULL PRIMARY KEY,
                    frequent_2021 INTEGER,
                    frequent_2022 INTEGER,
                    frequent_2023 INTEGER
                )
                """)

connexion.commit()

curseur.execute("DROP TABLE IF EXISTS lumiere")
curseur.execute(""" CREATE TABLE IF NOT EXISTS lumiere(
                    date TEXT NOT NULL PRIMARY KEY,
                    cloud INTEGER,
                    sun INTEGER
                
                   
                )
                """)

curseur.execute("DROP TABLE IF EXISTS objets_trouves")
curseur.execute("""
                CREATE TABLE IF NOT EXISTS objets_trouves(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL ,
                    type TEXT ,
                    gare TEXT ,
                    FOREIGN KEY (date) REFERENCES lumiere(date)
                    
                )
                """)

connexion.commit()
connexion.close()

# curseur.execute(""" CREATE TABLE IF NOT EXISTS obj_semaine(
#                     week TEXT NOT NULL PRIMARY KEY,
#                     obj_trouves INTEGER
                   
#                 )
#                 """)

# connexion.commit()

# curseur.execute("""
#                 CREATE TABLE IF NOT EXISTS objets_trouves(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     date TEXT NOT NULL PRIMARY KEY ,
#                     type TEXT ,
#                     gare TEXT ,
#                     nom_gare TEXT ,
#                     date_meteo TEXT NULL,
#                     FOREIGN KEY (nom_gare) REFERENCES gare(nom_gare),
#                     FOREIGN KEY (date_meteo) REFERENCES meteo(date)
#                 )
#                 """)

# connexion.commit()


