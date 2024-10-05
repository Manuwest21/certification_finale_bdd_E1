
import pyodbc


conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

# Connexion à la base de données Azure
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

# Supprimer les tables existantes si elles existent
cursor_azure.execute("DROP TABLE IF EXISTS objets_trouves9")
cursor_azure.execute("DROP TABLE IF EXISTS lumiere9")
cursor_azure.execute("DROP TABLE IF EXISTS frequentation9")

# Création de la table 'lumiere9'
cursor_azure.execute(""" 
    CREATE TABLE lumiere9(
        date DATE PRIMARY KEY,
        cloud VARCHAR(255) NOT NULL,
        sun VARCHAR(255) NOT NULL
    )
""")

# Création de la table 'frequentation9' avec gare comme clé primaire
cursor_azure.execute(""" 
    CREATE TABLE frequentation9(
        gare VARCHAR(255) PRIMARY KEY,
        frequent_2021 INTEGER NOT NULL,
        frequent_2022 INTEGER NOT NULL,
        frequent_2023 INTEGER NOT NULL
    )
""")

# Création de la table 'objets_trouves9' avec des clés étrangères
cursor_azure.execute(""" 
    CREATE TABLE objets_trouves9(
        id INT PRIMARY KEY IDENTITY(1,1),
        date DATE NOT NULL,
        type VARCHAR(255) NOT NULL,
        gare VARCHAR(255) NOT NULL,
        poids_pondere FLOAT,
        FOREIGN KEY (date) REFERENCES lumiere9(date),
        FOREIGN KEY (gare) REFERENCES frequentation9(gare)
    )
""")

# Valider les modifications
conn_azure.commit()

# Fermer la connexion
cursor_azure.close()
conn_azure.close()