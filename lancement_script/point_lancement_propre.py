import sqlite3
import requests
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Point de lancement
def main():
    try:
        # Initialisation des dépendances et des connexions externes
        conn = sqlite3.connect('bdd_objets_luminosite.db')
        cursor = conn.cursor()

        # Initialisation des tables dans la base de données
        initialize_database(cursor)
        
        # Règles logiques de traitement
        process_data(cursor)

        # Sauvegarde des résultats
        save_results(cursor, conn)

    except Exception as e:
        # Gestion des erreurs et des exceptions
        logging.error(f"Une erreur est survenue : {e}")
    finally:
        # Fin du traitement
        conn.close()
        logging.info("Connexion à la base de données fermée.")

def initialize_database(cursor):
    """ Initialise les tables dans la base de données. """
    try:
        cursor.execute("DROP TABLE IF EXISTS frequentation")
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS frequentation (
                nom_gare TEXT NOT NULL PRIMARY KEY,
                frequent_2021 INTEGER,
                frequent_2022 INTEGER,
                frequent_2023 INTEGER
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS lumiere")
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS lumiere (
                date TEXT NOT NULL PRIMARY KEY,
                cloud INTEGER,
                sun INTEGER
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS objets_trouves")
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS objets_trouves (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT,
                gare TEXT,
                FOREIGN KEY (date) REFERENCES lumiere(date)
            )
        """)
        
        logging.info("Tables initialisées avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de l'initialisation de la base de données : {e}")
        raise

def process_data(cursor):
    """ Récupère et insère les données dans les tables. """
    try:
        # Exemple de récupération des données depuis une API
        response = requests.get('https://api.exemple.com/data')
        data = response.json()

        # Traitement des données (ajustez en fonction des besoins)
        for item in data['items']:
            cursor.execute("""
                INSERT INTO frequentation (nom_gare, frequent_2021, frequent_2022, frequent_2023)
                VALUES (?, ?, ?, ?)
            """, (item['nom_gare'], item['frequent_2021'], item['frequent_2022'], item['frequent_2023']))

        logging.info("Données traitées et insérées avec succès.")
    except requests.RequestException as e:
        logging.error(f"Erreur de requête API : {e}")
        raise
    except sqlite3.DatabaseError as e:
        logging.error(f"Erreur de base de données : {e}")
        raise

def save_results(cursor, conn):
    """ Sauvegarde les résultats et effectue un commit. """
    try:
        conn.commit()
        logging.info("Les résultats ont été sauvegardés.")
    except sqlite3.DatabaseError as e:
        logging.error(f"Erreur lors de la sauvegarde des résultats : {e}")
        conn.rollback()
        raise

if __name__ == "__main__":
    main()
