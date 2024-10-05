# Connexion à SQL Azure
import pyodbc


conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'



# connexion à ma base de donnée Azure
# conn_str=**ODBC_version*****nom_serveur_azure***nom base de donnée***nom utilisateur*****mot_de_passe*** 

conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

# Connexion à la base de données Azure via pyodbc 
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

# Création de la table 'lumiere' 
cursor_azure.execute(""" 
    CREATE TABLE lumiere(
        date DATE PRIMARY KEY,
        cloud INTEGER NOT NULL,
        sun INTEGER NOT NULL
        FOREIGN KEY (date) REFERENCES objets_trouves(date)
    )
""")

# Création de la table 'objets_trouves' 
cursor_azure.execute(""" 
    CREATE TABLE objets_trouves(
        id INT PRIMARY KEY IDENTITY(1,1),
        date DATE,
        type VARCHAR(20) NOT NULL,
        gare TEXT NOT NULL,
        poids_pondere FLOAT
        FOREIGN KEY (date) REFERENCES lumiere(date)
        FOREIGN KEY (gare) REFERENCES frequentation(gare)
    )
""")

# Création de la table 'frequentation' 
cursor_azure.execute(""" 
    CREATE TABLE frequentation(
        gare TEXT PRIMARY KEY,
        frequent_2021 INTEGER NOT NULL,
        frequent_2022 INTEGER NOT NULL,
        frequent_2023 INTEGER NOT NULL
        FOREIGN KEY (gare) REFERENCES objets_trouves(gare)
    )
""")

# Validation des modifications dans la base de données
conn_azure.commit()

# Fermeture de la connexion à la base de données
conn_azure.close()


cursor_azure.execute("DROP TABLE IF EXISTS frequentation")


#cursor_azure.execute("DROP TABLE IF EXISTS frequentation")
cursor_azure.execute(""" 
    CREATE TABLE lumiere9(
        date DATE PRIMARY KEY,
        cloud VARCHAR(255) NOT NULL,
        sun VARCHAR(255) NOT NULL
    )
""")


cursor_azure.execute(""" 
    CREATE TABLE objets_trouves9(
        id INT PRIMARY KEY IDENTITY(1,1),
        date DATE,
        type VARCHAR(255) NOT NULL,
        gare VARCHAR(255) NOT NULL,
        
    )
""")


cursor_azure.execute(""" 
    CREATE TABLE frequentation9(
        gare TEXT PRIMARY KEY IDENTITY(1,1),
        frequent_2021 VARCHAR(255) NOT NULL,
        frequent_2022 VARCHAR(255) NOT NULL,
        frequent_2023 VARCHAR(255) NOT NULL
    )
""")


poids_pondere FLOAT