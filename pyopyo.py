import pyodbc
import re
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime

server='rg-devries-serveur.database.windows.net'
database='luminosite-devries'
username = 'manu21'
password = '*Servor1'
driver = 'ODBC Driver 18 for SQL Server'
print(password)
print(server)
print(database)
print(driver)
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()



cursor.execute("DROP TABLE IF EXISTS scrapings")
cursor.execute(""" 
       CREATE TABLE scrapings(
            id INT PRIMARY KEY IDENTITY(1,1),
            title TEXT NOT NULL,
            distributeur TEXT NOT NULL,
            genre TEXT NOT NULL,
            dati TEXT NOT NULL)
            """)

# Valider la transaction
conn.commit()

# Fermer le curseur et la connexion
cursor.close()
conn.close()