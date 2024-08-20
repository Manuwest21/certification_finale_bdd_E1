import sqlite3

# Connexion à l'ancienne base de données
conn_old = sqlite3.connect('bddG.db')
cursor_old = conn_old.cursor()

# Récupérer les données combinées
query = '''
    SELECT 
        objets_trouves.data AS date,
  
        objets_trouves.nom_gare,
        lumiere.cloud,
        lumiere.sun
    FROM 
        objets_trouves
    INNER JOIN 
        lumiere
    ON 
        objets_trouves.data = lumiere.date
'''
cursor_old.execute(query)
combined_data = cursor_old.fetchall()

# Connexion à la nouvelle base de données
conn_new = sqlite3.connect('combi.db')
cursor_new = conn_new.cursor()

# Créer la nouvelle table dans la nouvelle base de données
cursor_new.execute('''
    CREATE TABLE combined_table (
        date TEXT,
        description TEXT,
        nom_gare TEXT,
        cloud TEXT,
        sun TEXT
    )
''')

# Insérer les données combinées dans la nouvelle table
cursor_new.executemany('''
    INSERT INTO combined_table (date, description, nom_gare, cloud, sun)
    VALUES (?, ?, ?, ?, ?)
''', combined_data)

# Commit et fermer les connexions
conn_new.commit()
conn_old.close()
conn_new.close()

print("Les données combinées ont été insérées dans combi.db avec succès.")