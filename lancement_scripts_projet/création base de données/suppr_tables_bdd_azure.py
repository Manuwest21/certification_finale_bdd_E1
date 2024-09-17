import pyodbc

conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rg-devries-serveur.database.windows.net;DATABASE=luminosite-devries;UID=manu21;PWD=*Servor1'
conn_azure = pyodbc.connect(conn_str)
cursor_azure = conn_azure.cursor()

# Suppression des tables si elles existent
cursor_azure.execute("DROP TABLE IF EXISTS lumieri")
cursor_azure.execute("DROP TABLE IF EXISTS objets_trouvis")
cursor_azure.execute("DROP TABLE IF EXISTS frequentati")

# Commit des transactions pour appliquer les suppressions
conn_azure.commit()

# Fermer la connexion SQL Azure
conn_azure.close()