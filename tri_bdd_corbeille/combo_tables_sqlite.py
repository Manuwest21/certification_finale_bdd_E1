import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('bddt.db')
cursor = conn.cursor()

# Créer la nouvelle table
cursor.execute('''
    CREATE TABLE combined_table4 AS
    SELECT 
        objets_trouves.data AS date,
         objets_trouves.typo AS type,
        objets_trouves.nom_gare,
        lumiere.cloud,
        lumiere.sun
    FROM 
        objets_trouves
    INNER JOIN 
        lumiere
    ON 
        objets_trouves.data = lumiere.date
''')

# Vérifier que la table a été créée
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Afficher le contenu de la nouvelle table
cursor.execute('SELECT * FROM combined_table4')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fermer la connexion
conn.close()