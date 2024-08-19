import pypyodbc

# Remplacez ces valeurs par vos informations de connexion
server = 'rg-devries-serveur.database.windows.net'
database = 'luminosite-devries'
username = 'manu21'
password = '*Servor1'
driver = '{ODBC Driver 18 for SQL Server}'

# Chaîne de connexion
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Établir la connexion
    conn = pypyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Exécuter une requête SQL pour créer une table
    cursor.execute('''
    CREATE TABLE Gare_lumiere (
        CustomerID INT PRIMARY KEY,
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50),
        Email NVARCHAR(100)
    );
    ''')

    # Valider la transaction
    conn.commit()

    print("Table created successfully.")

except pyodbc.Error as e:
    print(f"Error: {e}")

finally:
    # Fermer la connexion
    cursor.close()
    conn.close()