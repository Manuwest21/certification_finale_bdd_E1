import pandas as pd
import requests
import sqlite3

# Initialisation du DataFrame avec les colonnes appropriées
df = pd.DataFrame(columns=['date', 'type', 'gare'])

def replace_apostrophes(text):
    return text.replace("'", "''") if text else text

i = 0
gares_parisiennes = ['Gare du Nord', 'Gare de Lyon']  # Remplacez par vos gares
annees = ['2023', '2022']  # Remplacez par vos années

for gare in gares_parisiennes:
    for annee in annees:
        print(i)
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}")
        records = response.json()
        print(records)
        
        for record in records['records']:
            print(i)
            date = record['fields'].get('date', '')
            type = replace_apostrophes(record['fields'].get('gc_obo_type_c', ''))
            gare = replace_apostrophes(record['fields'].get('gc_obo_gare_origine_r_name', ''))
            
            # Ajouter les données au DataFrame
            df = df.append({'date': date, 'type': type, 'gare': gare}, ignore_index=True)
            
            # Insérer les données dans la base de données SQLite
            connexion = sqlite3.connect("bdd_luz.db")
            curseur = connexion.cursor()
            curseur.execute("""
                INSERT INTO objets_trouves (date, type, gare)
                VALUES (?, ?, ?)
            """, (date, type, gare))
            connexion.commit()
            connexion.close()
            
            i += 1

# Optionnel : sauvegarder le DataFrame dans un fichier CSV pour vérification
df.to_csv('objets_trouves.csv', index=False)
