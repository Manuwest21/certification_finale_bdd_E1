import pyodbc


server='rg-devries-serveur.database.windows.net'
database='luminosite-devries'
username = 'manu21'
password = '*Servor1'
driver = 'ODBC Driver 18 for SQL Server'
-- print(password)
-- print(server)
-- print(database)
-- print(driver)
import pyodbc
server='rg-ds-serveur.database.windows.net'
database='luminosit'
username = 'ma1'
password = '*Se1'
driver = 'ODBC Driver 18 for SQL Server'
# Informations de connexion


# Connexion à la base de données
conn_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Suppression de la table si elle existe déjà
cursor.execute("DROP TABLE IF EXISTS frequentation")

# Création de la table
cursor.execute("""
    CREATE TABLE frequentation (
        id INT PRIMARY KEY IDENTITY(1,1),
        gare VARCHAR(10),
        frequent_2021 INTEGER,
        frequent_2022 INTEGER,
        frequent_2023 INTEGER,
    )
""")

# Valider la transaction
conn.commit()

# Fermer le curseur et la connexion
cursor.close()
conn.close()
