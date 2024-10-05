import os
import pandas as pd

# Une liste est faîte avec le nom des fichiers CSV à concaténer
csv_file = []

# Ajouter les fichiers CSV pour chaque dossier (2021, 2022, 2023)
for i in range(1, 13):
    csv_file.append(f'export-paris21_{i}.csv')  # Fichiers de "meteo_2021"
for i in range(1, 13):
    csv_file.append(f'paris22_{i}.csv')  # Fichiers de "meteo_2022"
for i in range(1, 13):
    csv_file.append(f'paris23_{i}.csv')  # Fichiers de "meteo_2023"

# Initialiser une liste pour stocker les DataFrames de chaque fichier CSV
dfs = []

# Dossier parent contenant les sous-dossiers "meteo_2021", "meteo_2022", "meteo_2023"
main_folder = 'csv_meteo'  # Remonter d'un dossier avec "../"

# Lire chaque fichier CSV dans un DataFrame et l'ajouter à la liste
for idx, file in enumerate(csv_file):
    # Déterminer l'année à partir de l'index et choisir le bon sous-dossier
    if idx < 12:     
        year_folder = 'meteo_2021'
    # pour les 12 premiers éléments de la liste, une association est faîte avec un nom de dossier
    elif idx < 24:
        year_folder = 'meteo_2022'
    # pour les éléments de 13 à 24, association d'un nom de sous-dossier
    else:
        year_folder = 'meteo_2023'
    # pour les éléments au delà de la position 24 dans la liste, association d'un nom de sous-dossier
        
    # Construire le chemin complet du fichier CSV
    csv_path = os.path.join(main_folder, year_folder, file)
    
    # Lire le fichier CSV en sautant les 3 premières lignes de texte
    try:
        df = pd.read_csv(csv_path, skiprows=3)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {csv_path}: {e}")
        continue
    
    # Ajouter le DataFrame à la liste
    dfs.append(df)

# Concaténer tous les DataFrames en un seul DataFrame
result = pd.concat(dfs, ignore_index=True)

# Chemin vers le répertoire de lancement du script
output_dir = os.getcwd()

# Construire le chemin complet pour le fichier CSV de sortie
# output_file = os.path.join(output_dir, '../../csv_modélisé/all_meteo.csv')
output_file = os.path.join(output_dir, 'csv_modélisé/all_meteo.csv')
# Écrire la DataFrame résultante dans le fichier CSV
result.to_csv(output_file, index=False)

# Afficher un message de confirmation
print(f"Concaténation terminée avec succès ! Le fichier CSV a été enregistré dans '{output_file}'.")

