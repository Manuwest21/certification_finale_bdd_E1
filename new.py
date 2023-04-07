import requests
import pandas as pd
import os 

gares_parisiennes = ["Paris Gare de Lyon", "Paris Montparnasse", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , 'Paris Bercy']
annees = ["2019", "2020" , "2021" , "2022"]
voyageurs_an=['total_voyageurs_non_voyageurs_2019','total_voyageurs_2019','total_voyageurs_non_voyageurs_2020','total_voyageurs_2020','total_voyageurs_non_voyageurs_2021','total_voyageurs_2021','total_voyageurs_non_voyageurs_2022','total_voyageurs_2022']
# Création d'un DataFrame vide
df = pd.DataFrame()
i = 0
for gare in gares_parisiennes:
    for annee in annees:
        print(i)
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}")
        #on demande la réponse à la requête get pour obtenir les données de 
        print (response)
        # Récupération des enregistrements
        records= response.json()
        print(records)
        df = pd.json_normalize(records["records"])
        # Enregistrer les données dans un fichier CSV avec le nom de la gare
        filename = f"{gare}{annee}.csv"
        df.to_csv(filename, index=False)
        i
    # else:
    #     # Conversion des enregistrements en DataFrame
    #     records_df = pd.DataFrame([record["fields"] for record in records])

    #     # Ajout des enregistrements au DataFrame global
        i
    #     df = pd.concat([df, records_df], ignore_index=True)
    #     i += 1
        
# df.to_csv("objets_trouves.csv", index=False)



# Chemin du dossier contenant les fichiers CSV
folder_path = "/home/apprenant/Documents/objets_trouves"

# Liste pour stocker les DataFrames
df_list = []

# Boucle sur les fichiers CSV dans le dossier
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        # Chemin complet du fichier CSV
        file_path = os.path.join(folder_path, file_name)
        # Lecture du fichier CSV en tant que DataFrame et ajout à la liste
        df_list.append(pd.read_csv(file_path))

# Concaténation des DataFrames en un seul
concatenated_df = pd.concat(df_list)

# Affichage du DataFrame concaténé
print(concatenated_df)