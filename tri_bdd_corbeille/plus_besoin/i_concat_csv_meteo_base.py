import pandas as pd
import os

# Chemins vers les répertoires contenant les fichiers CSV
chemins_repertoires = ["met_pa_2021/", "met_pa_2022/", "met_pa_2023/"]

# Initialiser une liste pour stocker les DataFrames de chaque fichier CSV
dfs = []

# Parcourir tous les répertoires
for chemin_repertoire in chemins_repertoires:
    # Parcourir tous les fichiers dans le répertoire
    for nom_fichier in os.listdir(chemin_repertoire):
        if nom_fichier.endswith(".csv"):
            chemin_fichier = os.path.join(chemin_repertoire, nom_fichier)
            
            # Lire le fichier CSV dans un DataFrame
            df = pd.read_csv(chemin_fichier, skiprows=3, sep='\t')
            
            # Ajouter le DataFrame à la liste
            dfs.append(df)

# Concaténer les DataFrames dans une seule DataFrame
result = pd.concat(dfs, ignore_index=True)

# Écrire la DataFrame résultante dans un nouveau fichier CSV
chemin_fichier_concatene = "concat_meteo_years.csv"
result.to_csv(chemin_fichier_concatene, index=False)
