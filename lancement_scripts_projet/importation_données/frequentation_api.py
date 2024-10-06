import requests
import pandas as pd
import sqlite3

gare = ["Paris Gare de Lyon", "Paris Montparnasse", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , "Paris Bercy Bourgogne - Pays d\'Auvergne"]

annees = [ "2021", "2022","2023"]
voyageurs_an=['total_voyageurs_non_voyageurs_2021','total_voyageurs_2021','total_voyageurs_non_voyageurs_2022','total_voyageurs_2022','total_voyageurs_non_voyageurs_2023','total_voyageurs_2023']
df = pd.DataFrame(columns=["gare", "frequent_2021", "frequent_2022","frequent_2023"])
for i in gare:
                                                           
    response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=frequentation-gares&q={i}&sort=nom_gare&facet=nom_gare&refine.nom_gare={i}")
    frequent=response.json()
    # print(frequent)
    # Vérifier s'il y a des enregistrements
    if frequent['records']:  # Vérifie si la liste n'est pas vide
        # Extraire les champs des données
        frequent = frequent['records'][0]['fields']
        print(frequent)  # Afficher les données
    
        frequent_2021=frequent['total_voyageurs_non_voyageurs_2021']+frequent['total_voyageurs_2021']
        frequent_2022=frequent['total_voyageurs_non_voyageurs_2022']+frequent['total_voyageurs_2022']
        frequent_2023=frequent['total_voyageurs_non_voyageurs_2023']+frequent['total_voyageurs_2023']
        print (frequent_2021)


        new_row = {"gare": i,  "frequent_2021": frequent_2021, "frequent_2022": frequent_2022, "frequent_2023": frequent_2023}

        df = df._append(new_row, ignore_index=True)
    
    else:
        print(f"Aucune donnée trouvée pour {i}.")  # Afficher un message si aucune donnée n'est trouvée

print (df)    
   
# df.to_csv("csv_modélisé/frequentation.csv")
df.to_csv("csv_modélisé/frequentation1.csv")