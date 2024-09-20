# Connexion à SQL Azure
import pyodbc


conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()





conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

cursor_azure.execute("DROP TABLE IF EXISTS frequentation")
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
        poids_pondere FLOAT
    )
""")


cursor_azure.execute(""" 
    CREATE TABLE frequentation9(
        id INT PRIMARY KEY IDENTITY(1,1),
        gare TEXT ,
        frequent_2021 VARCHAR(255) NOT NULL,
        frequent_2022 VARCHAR(255) NOT NULL,
        frequent_2023 VARCHAR(255) NOT NULL
    )
""")


conn_azure.commit()


conn_azure.close()



