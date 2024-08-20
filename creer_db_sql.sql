-- Créer la base de données influx_lu
CREATE DATABASE influence_luminosite;

-- Sélectionner la base de données influx_lu pour les opérations suivantes


-- Créer la table lumiere
CREATE TABLE lumiere (
    date DATE PRIMARY KEY,
    cloud INT,
    sun DECIMAL(5, 2)
);

-- Créer la table objets_trouves
CREATE TABLE objets_trouves (
    date DATE,
    type VARCHAR(255),
    gare VARCHAR(255),
    PRIMARY KEY (date, type, gare)
);
import sqlite3

# Connexion à la base de données SQLite
conn_sqlite = sqlite3.connect('bdd_luz.db')
cursor_sqlite = conn_sqlite.cursor()

# Extraire les données de la table 'lumiere'
cursor_sqlite.execute("SELECT * FROM lumiere")
data_lumiere = cursor_sqlite.fetchall()

# Extraire les données de la table 'objets_trouves'
cursor_sqlite.execute("SELECT * FROM objets_trouves")
data_objets_trouves = cursor_sqlite.fetchall()
print(data_lumiere)
# Fermer la connexion SQLite
conn_sqlite.close()
-- Insérer des données d'exemple dans la table lumiere
-- INSERT INTO lumiere (date, cloudcover, sunhour) VALUES ('2024-08-19', 75, 7.5);
-- INSERT INTO lumiere (date, cloudcover, sunhour) VALUES ('2024-08-20', 80, 6.0);

-- -- Insérer des données d'exemple dans la table objets_trouves
-- INSERT INTO objets_trouves (date, type, gare) VALUES ('2024-08-19', 'Bagage', 'Gare du Nord');
-- INSERT INTO objets_trouves (date, type, gare) VALUES ('2024-08-20', 'Clé', 'Gare de Lyon');
