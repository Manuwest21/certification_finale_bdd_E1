import os
import pandas as pd

# Liste des noms de fichiers CSV à concaténer
csv_file = []  # Liste des noms de fichiers CSV

# Ajout des fichiers CSV de chaque dossier (2021, 2022, 2023)
for i in range(1, 13):
    csv_file.append(f'meteo_2021/export-paris21_{i}.csv')  # Fichiers de "meteo_2021"
for i in range(1, 13):
    csv_file.append(f'meteo_2022/paris22_{i}.csv')  # Fichiers de "meteo_2022"
for i in range(1, 13):
    csv_file.append(f'meteo_2023/paris23_{i}.csv')  # Fichiers de "meteo_2023"

# Dossier où se trouvent les fichiers CSV
base_folder = 'csv_meteo'

# On initialise une liste pour stocker les DataFrames de chaque fichier CSV
dfs = []

# Lire chaque fichier CSV dans un DataFrame et l'ajouter à la liste
for file_name in csv_file:
    # Construire le chemin complet du fichier CSV
    csv_path = os.path.join(base_folder, file_name)  
    # Lire le fichier CSV dans un DataFrame
    df = pd.read_csv(csv_path, skiprows=3)  
    # Ajouter le DataFrame à la liste
    dfs.append(df)

# Concaténer des DataFrames dans un seul DataFrame
result = pd.concat(dfs, ignore_index=True)

# Création d'un nouveau fichier CSV à partir des CSV concaténés
result.to_csv('all_meteo.csv', index=False)
# Message de succés au processus
print("Concaténation terminée avec succès !")