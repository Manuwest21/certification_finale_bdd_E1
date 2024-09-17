import requests
import pandas as pd
import sqlite3

gare = ["Paris Gare de Lyon", "Paris Montparnasse", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , "Paris Bercy Bourgogne - Pays d'Auvergne"]

annees = [ "2021", "2022","2023"]
voyageurs_an=['total_voyageurs_non_voyageurs_2021','total_voyageurs_2021','total_voyageurs_non_voyageurs_2022','total_voyageurs_2022','total_voyageurs_non_voyageurs_2023','total_voyageurs_2023']
df = pd.DataFrame(columns=["gare", "frequent_2021", "frequent_2022","frequent_2023"])
for i in gare:
                                                             #  /api/records/1.0/search/?dataset=frequentation-gares&q=paris+gare+de+lyon&sort=nom_gare&facet=nom_gare&refine.nom_gare=Paris+Gare+de+Lyon 
    response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=frequentation-gares&q={i}&sort=nom_gare&facet=nom_gare&refine.nom_gare={i}")
    frequent=response.json()
   
    frequent=frequent['records'][0]['fields']
    print(frequent)
    
    
    
    frequent_2021=frequent['total_voyageurs_non_voyageurs_2021']+frequent['total_voyageurs_2021']
    frequent_2022=frequent['total_voyageurs_non_voyageurs_2022']+frequent['total_voyageurs_2022']
    frequent_2023=frequent['total_voyageurs_non_voyageurs_2023']+frequent['total_voyageurs_2023']
    print (frequent_2021)
    #df = pd.DataFrame({
    #     "gare":[]
   # "frequent": [frequent_2019, frequent_2020, frequent_2021],


    new_row = {"gare": i,  "frequent_2023": frequent_2023, "frequent_2021": frequent_2021, "frequent_2022": frequent_2022}

    df = df._append(new_row, ignore_index=True)

    
    # })
    connexion = sqlite3.connect("bdd_luz_actu3.db")
    curseur = connexion.cursor()
    curseur.execute("""
        INSERT INTO frequentation (nom_gare,  frequent_2021, frequent_2022, frequent_2023)
        VALUES
        ("{}",'{}','{}','{}')
    """.format(i,int(frequent_2021),int(frequent_2022),int(frequent_2023) ))
    connexion.commit()
    connexion.close()
df.to_csv("frequentation_actu.csv")