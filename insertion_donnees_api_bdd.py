import requests
import pandas as pd
import sqlite3
gares_parisiennes = ["Paris Gare de Lyon", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , 'Paris Bercy']
annees = ["2019,2020,2021,2022"]

# Création d'un DataFrame vide
df = pd.DataFrame()
i = 0
for gare in gares_parisiennes:
    for annee in annees:
        print(i)
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}")
        #on demande la réponse à la requête get pour obtenir les données de 
        # print (response)
        # Récupération des enregistrements
        records= response.json()
        
        for i in records['records']:
            dati = i['fields']['date']
            typo = i['fields']['gc_obo_type_c']
            gara = i['fields']['gc_obo_gare_origine_r_name']
            connexion = sqlite3.connect("bddd.db")
            curseur = connexion.cursor()
            curseur.execute("""
                INSERT INTO objets_trouves (data,typo,nom_gare)
                VALUES
                ('{}','{}','{}')
            """.format(dati, typo, gara))
            connexion.commit()