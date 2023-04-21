import requests
import pandas as pd
import sqlite3

gare = ["Paris Gare de Lyon", "Paris Montparnasse", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , "Paris Bercy Bourgogne - Pays d'Auvergne"]

annees = ["2019", "2020" , "2021" , "2022"]
voyageurs_an=['total_voyageurs_non_voyageurs_2019','total_voyageurs_2019','total_voyageurs_non_voyageurs_2020','total_voyageurs_2020','total_voyageurs_non_voyageurs_2021','total_voyageurs_2021','total_voyageurs_non_voyageurs_2022','total_voyageurs_2022']
df = pd.DataFrame(columns=["gare", "frequent_2019", "frequent_2020", "frequent_2021", "frequent_2022"])
for i in gare:
                                                             #  /api/records/1.0/search/?dataset=frequentation-gares&q=paris+gare+de+lyon&sort=nom_gare&facet=nom_gare&refine.nom_gare=Paris+Gare+de+Lyon 
    response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=frequentation-gares&q={i}&sort=nom_gare&facet=nom_gare&refine.nom_gare={i}")
    frequent=response.json()
   
    frequent=frequent['records'][0]['fields']
    print(frequent)
    
    frequent_2019=frequent['total_voyageurs_non_voyageurs_2019']+frequent['total_voyageurs_2019']
    frequent_2020=frequent['total_voyageurs_non_voyageurs_2020']+frequent['total_voyageurs_2020']
    frequent_2021=frequent['total_voyageurs_non_voyageurs_2021']+frequent['total_voyageurs_2021']
    frequent_2022=frequent['total_voyageurs_non_voyageurs_2021']+frequent['total_voyageurs_2021']
    print (frequent_2019)
    #df = pd.DataFrame({
    #     "gare":[]
   # "frequent": [frequent_2019, frequent_2020, frequent_2021],


    new_row = {"gare": i, "frequent_2019": frequent_2019, "frequent_2020": frequent_2020, "frequent_2021": frequent_2021, "frequent_2022": frequent_2022}

    df = df.append(new_row, ignore_index=True)

    
    # })
    connexion = sqlite3.connect("bddp.db")
    curseur = connexion.cursor()
    curseur.execute("""
        INSERT INTO gare (nom_gare, frequent_2019, frequent_2020, frequent_2021, frequent_2022)
        VALUES
        ("{}",'{}','{}','{}','{}')
    """.format(i,int(frequent_2019), int(frequent_2020), int(frequent_2021),int(frequent_2021)))
    connexion.commit()
df.to_csv("frequentation.csv")