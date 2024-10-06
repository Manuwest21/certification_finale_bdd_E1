import requests
import pandas as pd
import sqlite3
import sys 
gares_parisiennes = ["Paris Gare de Lyon"]
# ici l'ensemble des gares parisiennes qui nous intéressent 
annees = ["2021"]
# ici l'ensemble des années pour lesquelles on veut recueillir des données

def replace_apostrophes(text):
    return text.replace("'", " ")
# Création d'un DataFrame vide
df = pd.DataFrame()
i = 0
for gare in gares_parisiennes:
    for annee in annees:
        
        print(i)
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}")
        #on demande la réponse à la requête get pour obtenir les données de 
        print (response.text )
        print(response.content)
        exit()
        print(response.json())

        exit()
        print("a")
        # Récupération des enregistrements
        records= response.json()
        print(records)
        nombre= 12
        for i in records['records']:
            nombre+=1
            print(nombre)
          
            
            dati = i['fields']['date']
            print("1")
            typo = i['fields']['gc_obo_type_c']
            typo = replace_apostrophes(i['fields']['gc_obo_type_c'])

            print("2")
            gara = i['fields']['gc_obo_gare_origine_r_name']
            gara = replace_apostrophes(i['fields']['gc_obo_gare_origine_r_name'])
            print("3")
            connexion = sqlite3.connect("bdd_luz.db")
            curseur = connexion.cursor()
            curseur.execute("""
                INSERT INTO objets_trouves (date,type,gare)
                VALUES
                ('{}','{}','{}')
            """.format(dati, typo, gara))
            connexion.commit()