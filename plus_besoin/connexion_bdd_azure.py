import pyodbc
import sqlalchemy
from sqlalchemy import create_engine

server = 'certifmanu1.database.windows.net'
database = 'manumanu'
username = 'manumanu'
password = '*certifcertif1'
driver = '{ODBC Driver 18 for SQL Server}'

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

# Exemple d'insertion de données
with engine.connect() as conn:
    conn.execute("INSERT INTO your_table (column1, column2) VALUES ('value1', 'value2')")