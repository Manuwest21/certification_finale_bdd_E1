
import pyodbc


conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()





conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

cursor_azure.execute("DROP TABLE IF EXISTS lumiere")
cursor_azure.execute(""" 
    CREATE TABLE lumiere(
        date DATE PRIMARY KEY,
        cloud FLOAT NOT NULL,
        sun FLOAT NOT NULL
    )
""")

cursor_azure.execute("DROP TABLE IF EXISTS objets_trouves")
cursor_azure.execute(""" 
    CREATE TABLE objets_trouves(
        id INT PRIMARY KEY IDENTITY(1,1),
        date TEXT,
        type VARCHAR(25) NOT NULL,
        gare VARCHAR(25) NOT NULL,
        poids_pondere FLOAT
    )
""")

cursor_azure.execute("DROP TABLE IF EXISTS frequentation")
cursor_azure.execute(""" 
    CREATE TABLE frequentation(
        id INT PRIMARY KEY IDENTITY(1,1),
        gare TEXT ,
        frequent_2021 INT NOT NULL,
        frequent_2022 INT NOT NULL,
        frequent_2023 INT NOT NULL
    )
""")


conn_azure.commit()


conn_azure.close()



