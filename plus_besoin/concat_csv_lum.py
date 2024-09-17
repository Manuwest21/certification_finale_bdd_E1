import pandas as pd

# Liste des noms de fichiers CSV à concaténer
csv_file = []

for i in range(1, 10):
    csv_file.append(f'paris30{i}.csv')
# Ajout de paris201.csv jusqu'à paris2012.csv
for i in range(0, 4):
    csv_file.append(f'paris31{i}.csv')
for i in range(1, 10):
    csv_file.append(f'paris20{i}.csv')
for i in range(0, 4):
    csv_file.append(f'paris21{i}.csv')

# Ajout de paris202.csv jusqu'à paris20212.csv
for i in range(1, 13):
    csv_file.append(f'paris3{i:02d}.csv')

for i in range(1, 10):
    csv_file.append(f'paris10{i}.csv')
# Ajout de paris201.csv jusqu'à paris2012.csv
for i in range(0, 4):
    csv_file.append(f'paris11{i}.csv')

# Initialiser une liste pour stocker les DataFrames de chaque fichier CSV
dfs = []

# Lire chaque fichier CSV dans un DataFrame et l'ajouter à la liste
for idx, file in enumerate(csv_file):
    # Lire le fichier CSV dans un DataFrame
    df = pd.read_csv(file)
    
    # Si ce n'est pas le premier fichier, nommez le DataFrame de manière incrémentée
    if idx != 0:
        df.name = f"paris{200 + (idx // 12)}{idx % 12 + 1:02d}"

    # Ajouter le DataFrame à la liste
    dfs.append(df)

# Concaténer les DataFrames dans une seule DataFrame
result = pd.concat(dfs, ignore_index=True)

# Écrire la DataFrame résultante dans un nouveau fichier CSV
result.to_csv('concatenated_file_new.csv', index=False)