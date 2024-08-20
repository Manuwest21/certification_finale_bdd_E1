import sqlite3

# Connexion aux anciennes bases de données
conn_base1 = sqlite3.connect('bddt.db')
cursor_base1 = conn_base1.cursor()

conn_base2 = sqlite3.connect('bddG.db')
cursor_base2 = conn_base2.cursor()

# Récupérer les données de la table objets_trouves dans base1.db
query_objets_trouves = 'SELECT data, nom_gare FROM objets_trouves'
cursor_base1.execute(query_objets_trouves)
objets_trouves_data = cursor_base1.fetchall()

# Récupérer les données de la table lumiere dans base2.db
query_lumiere = 'SELECT date, cloud, sun FROM lumiere'
cursor_base2.execute(query_lumiere)
lumiere_data = cursor_base2.fetchall()

# Transformer les données lumiere en un dictionnaire pour un accès facile
lumiere_dict = {row[0]: (row[1], row[2]) for row in lumiere_data}

# Combiner les données sur les dates communes
combined_data = []
for data,  nom_gare in objets_trouves_data:
    if data in lumiere_dict:
        cloud, sun = lumiere_dict[data]
        combined_data.append((data,  nom_gare, cloud, sun))

# Connexion à la nouvelle base de données
conn_combi = sqlite3.connect('combi11.db')
cursor_combi = conn_combi.cursor()

# Créer la nouvelle table dans la nouvelle base de données
cursor_combi.execute('''
    CREATE TABLE combined_table (
        date TEXT,
        
        nom_gare TEXT,
        cloud TEXT,
        sun TEXT
    )
''')

# Insérer les données combinées dans la nouvelle table
cursor_combi.executemany('''
    INSERT INTO combined_table11 (date, nom_gare, cloud, sun)
    VALUES (?, ?, ?, ?)
''', combined_data)

# Commit et fermer les connexions
conn_combi.commit()
conn_base1.close()
conn_base2.close()
conn_combi.close()

print("Les données combinées ont été insérées dans combi11.db avec succès.")
