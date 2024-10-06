import requests
import pandas as pd
import sqlite3

gares_parisiennes = ["Paris Gare de Lyon", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , "Paris Bercy"]
# Liste des gares parisiennes

annees = ["2021","2022","2023"] # Liste des années
df = pd.DataFrame(columns=['date', 'type', 'gare'])    # création d'un dataframe vide avec en tête de colonnes
# Fonction pour remplacer les apostrophes
def replace_apostrophes(text):
    return text.replace("'", " ")

# Connexion à la base de données
connexion = sqlite3.connect("bdd_luminosite.db")
curseur = connexion.cursor()

# Boucle sur les gares et les années
for gare in gares_parisiennes:
    for annee in annees:
        print(f"Traitement de {gare} pour l'année {annee}")

        # Requête API
        url = f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}"
        response = requests.get(url)
        
        if response.status_code == 200:
            records = response.json()
            print(f"Nombre de records récupérés : {len(records['records'])}")
        #va nous renvoyer le nombre total d'enregistrements pour chaque couple année/gare
            
        # Insertion dans le DataFrame
            for record in records['records']:
                date = record['fields'].get('date', '')
                type_ = replace_apostrophes(record['fields'].get('gc_obo_type_c', ''))
                gare_ = replace_apostrophes(record['fields'].get('gc_obo_gare_origine_r_name', ''))
                date = record['fields'].get('date', '')
                type = replace_apostrophes(record['fields'].get('gc_obo_type_c', ''))
                gare = replace_apostrophes(record['fields'].get('gc_obo_gare_origine_r_name', ''))
            
            # Ajouter les données au DataFrame
                df = df._append({'date': date, 'type': type, 'gare': gare}, ignore_index=True)
        # Insertion dans la base de données
            # curseur.execute("""
            #         INSERT INTO objets_trouves (date, type, nom_gare)
            #         VALUES (?, ?, ?)
            #     """, (date, type_, gare_))
            # connexion.commit()
        else:
            print(f"Erreur {response.status_code} pour la requête : {url}")

# Fermeture de la connexion à la base de données
connexion.close()

# Affichage des premières lignes du DataFrame
print(df.head())
# df.to_csv('../../csv_modélisé/objets_trouves.csv', index=False)
df.to_csv('csv_modélisé/objets_trouves1.csv', index=False)