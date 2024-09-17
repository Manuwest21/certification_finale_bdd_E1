import os
import pandas as pd

# Chemin du dossier parent contenant les sous-dossiers "meteo_2021", "meteo_2022", "meteo_2023"
main_folder = 'csv_meteo'

# Initialisation d'une liste pour stocker les DataFrames de chaque fichier CSV
dfs = []

# Boucle sur les sous-dossiers "meteo_2021", "meteo_2022", "meteo_2023"
for year in ['meteo_2021', 'meteo_2022', 'meteo_2023']:
    folder_path = os.path.join(main_folder, year)
    
    # Liste des fichiers CSV dans le sous-dossier en question
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # Boucle sur chaque fichier CSV et ajout au DataFrame
    for csv_file in csv_files:
        csv_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(csv_path)
        dfs.append(df)

# Concaténation de tous les DataFrames en un seul
final_df = pd.concat(dfs, ignore_index=True)

# Affichage des premières lignes pour vérifier le résultat
print(final_df.head())