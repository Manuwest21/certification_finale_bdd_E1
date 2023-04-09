import sqlite3




connexion=sqlite3.connect('bddt.db')
curseur= connexion.cursor()

curseur.execute("""
                 UPDATE objets_trouves
                SET date_meteo = meteo.date
                FROM meteo
                WHERE objets_trouves.data = meteo.date
                 
                        """)
connexion.commit()
connexion.close()



connexion=sqlite3.connect('bddt.db')
curseur= connexion.cursor()

curseur.execute("""
                 UPDATE objets_trouves
                SET nom_gare = gare.nom_gare
                FROM gare
                WHERE objets_trouves.gare = gare.nom_gare
                 
                        """)
connexion.commit()
connexion.close()


