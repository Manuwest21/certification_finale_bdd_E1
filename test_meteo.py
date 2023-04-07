import requests
import pandas as pd
from datetime import datetime, timedelta

# API endpoint et clé d'API World Weather Online
url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
api_key = "b6d8416214ba4c30859123103230604"

# Paramètres de requête
params = {
     "key": api_key,
    "q": "Paris",
    "format": "json",
    "tp": "24", # Récupère les données toutes les 24 heures
}

# Début et fin de la période
start_date = datetime(2019, 1, 1)
end_date = datetime(2022, 12, 31)

# Liste qui contiendra les DataFrames pour chaque période de 35 jours
dfs = []

# Boucle sur les périodes de 35 jours maximum
while start_date <= end_date:
    end_period = start_date + timedelta(days=34)
    if end_period > end_date:
        end_period = end_date
    
    # Mise à jour des paramètres de requête avec les dates de la période
    params.update({"date": start_date.strftime("%Y-%m-%d"), "enddate": end_period.strftime("%Y-%m-%d")})
    
    # Envoi de la requête HTTP GET
    response = requests.get(url, params=params)

    # Vérification du code de réponse HTTP
    if response.status_code == 200:
        # Récupération des données au format JSON
        data = response.json()
        # Conversion des données JSON en DataFrame pandas
        df = pd.json_normalize(data["data"]["weather"])
        
        # Ajout du DataFrame de la période à la liste
        dfs.append(df)
    else:
        print("Erreur lors de la requête : code", response.status_code)
    
    # Mise à jour de la date de début de la période suivante
    start_date = end_period + timedelta(days=1)

# Concaténation de tous les DataFrames en un seul
final_df = pd.concat(dfs, ignore_index=True)

# Enregistrement du DataFrame au format CSV
final_df.to_csv("weather_data.csv", index=False)
