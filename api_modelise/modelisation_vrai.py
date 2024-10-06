import pyodbc
from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from datetime import date
from fastapi.routing import APIRouter
from securite_vrai import has_access  # Assurez-vous que cette fonction est définie correctement


# Connexion à la base de données Azure SQL
def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=rg-devries-serveur.database.windows.net;'
        'DATABASE=luminosite-devries;'
        'UID=manu21;'
        'PWD=*Servor1;'
    )
    return connection

app = APIRouter()

# Schémas Pydantic

class DateRange(BaseModel):
    start_date: date = Field(..., description="La date de début (Format: YYYY-MM-DD, entre 2021 et 2023)")
    end_date: date = Field(..., description="La date de fin (Format: YYYY-MM-DD, entre 2021 et 2023)")

    @validator('start_date', 'end_date')
    def validate_date_range(cls, value):
        if not (date(2021, 1, 1) <= value <= date(2023, 12, 31)):
            raise ValueError("La date doit être comprise entre 2021 et 2023")
        return value

class ObjetsTrouvesCreate(BaseModel):
    date: date
    type: str
    gare: str

class ObjetsTrouvesResponse(BaseModel):
    id: int
    date: date
    type: str
    gare: str

class FrequentationCreate(BaseModel):
    frequentation: int  

class FrequentationResponse(BaseModel):
    gare: str
    frequent_2021: int
    frequent_2022: int
    frequent_2023: int

class LumiereWithPoidsCreate(BaseModel):
    cloud: float = Field(..., description="Seuil de couverture nuageuse (0-100).")
    sun: float = Field(..., description="Heures d'ensoleillement par jour.")
    start_date: date = Field(..., description="Date de début de l'analyse (YYYY-MM-DD).", example="2023-01-01")
    end_date: date = Field(..., description="Date de fin de l'analyse (YYYY-MM-DD).", example="2023-12-31")

class LumiereWithPoidsResponse(BaseModel):
    somme_poids_pondere: Optional[float] = None

class ObjetsTrouvesCountResponse(BaseModel):
    total_count: int

@app.post("/objets_trouves/", response_model=ObjetsTrouvesResponse, dependencies=[Depends(has_access)])
def create_objets_trouves(objets_trouves: ObjetsTrouvesCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO objets_trouves (date, type, gare)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, objets_trouves.date, objets_trouves.type, objets_trouves.gare)
    connection.commit()
    cursor.close()
    connection.close()
    return objets_trouves

@app.get("/count_objets_trouves_gare/", dependencies=[Depends(has_access)])
def count_objets_trouves(
    start_date: date = Query(..., description="Date de début (Format: YYYY-MM-DD, entre 2021 et 2023)"),
    end_date: date = Query(..., description="Date de fin (Format: YYYY-MM-DD, entre 2021 et 2023)"),
    gare: Optional[str] = Query(None, description="La gare ou chercher (facultatif)")
):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    if gare:
        query = """
            SELECT COUNT(*)
            FROM objets_trouves9
            WHERE date BETWEEN ? AND ?
            AND gare = ?
        """
        cursor.execute(query, (start_date, end_date, gare))
    else:
        query = """
            SELECT COUNT(*)
            FROM objets_trouves
            WHERE date BETWEEN ? AND ?
        """
        cursor.execute(query, (start_date, end_date))
    
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if result:
        return {"total_count": result[0]}
    else:
        raise HTTPException(status_code=404, detail="pas de données correspondant aux critères")

@app.delete("/objets_trouves/{id}", response_model=ObjetsTrouvesResponse, dependencies=[Depends(has_access)])
def delete_objets_trouves(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM objets_trouves WHERE id = ?"
    cursor.execute(query, id)
    connection.commit()
    cursor.close()
    connection.close()
    return {"id": id}

@app.put("/frequentation/{gare}", response_model=FrequentationResponse, dependencies=[Depends(has_access)])
def update_frequentation(gare: str, frequentation: FrequentationCreate, year: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Vérifier si la gare existe avant de la mettre à jour
    cursor.execute("SELECT gare FROM frequentation WHERE gare = ?", (gare,))
    row = cursor.fetchone()
    
    if not row:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=404, detail="Gare not found")
    
    # Requête pour mettre à jour la fréquentation
    if year == 2021:
        query = "UPDATE frequentation9 SET frequent_2021 = ? WHERE gare = ?"
    elif year == 2022:
        query = "UPDATE frequentation9 SET frequent_2022 = ? WHERE gare = ?"
    elif year == 2023:
        query = "UPDATE frequentation9 SET frequent_2023 = ? WHERE gare = ?"
    else:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=400, detail="Invalid year")
    
    cursor.execute(query, (frequentation.frequentation, gare))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    # Récupérer et retourner les valeurs mises à jour
    cursor = connection.cursor()
    cursor.execute("SELECT gare, frequent_2021, frequent_2022, frequent_2023 FROM frequentation9 WHERE gare = ?", (gare,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if row:
        return FrequentationResponse(
            gare=row[0],
            frequent_2021=row[1],
            frequent_2022=row[2],
            frequent_2023=row[3]
        )
    else:
        raise HTTPException(status_code=404, detail="Frequentation data not found")
    
    

# @app.post("/cloud_sun/", response_model=LumiereWithPoidsResponse, dependencies=[Depends(has_access)])
# def calculate_poids_pondere(lumiere: LumiereWithPoidsCreate):
#     """
#     Cet endpoint permet de calculer la somme pondérée des poids des objets trouvés, 
#     en fonction de la couverture nuageuse et des heures d'ensoleillement pendant une période donnée.
    
#     L'utilisateur doit fournir :
#     - Le seuil de couverture nuageuse (cloud) [entre 0 et 100].
#     - Les heures d'ensoleillement (sun) [heures de soleil par jour].
#     - Une plage de dates (start_date, end_date) pour laquelle l'analyse doit être effectuée (de 2021-01-01 à 2023-12-31)
#     """
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     query = """
#         SELECT AVG(o.poids_pondere) AS somme_poids_pondere
#         FROM objets_trouves o
#         INNER JOIN lumiere l ON o.date = l.date
#         WHERE l.cloud < ? AND l.sun > ? AND o.date BETWEEN ? AND ?
#     """
    
    
#     cursor.execute(query, (lumiere.cloud, lumiere.sun, lumiere.start_date, lumiere.end_date))              # Exécution de la requête avec les valeurs de l'objet 'lumiere'
#     result = cursor.fetchone()

    
#     cursor.close()                                                                                         # Fermeture du curseur et de la connexion
#     connection.close()

   
#     if result:
#         return LumiereWithPoidsResponse(somme_poids_pondere=result[0])                                     # Vérification du résultat et retour de la réponse
#     else:
#         raise HTTPException(status_code=404, detail="Aucune donnée trouvée correspondant aux critères.")

@app.post("/cloud_sun/", response_model=LumiereWithPoidsResponse, dependencies=[Depends(has_access)])
def calculate_poids_pondere(
    cloud: float = Query(..., description="Seuil de couverture nuageuse minimale (0-100)"),
    sun: float = Query(..., description="Heures d'ensoleillement minimum par jour(1-15)"),
    start_date: date = Query(..., description="Date de début de l'analyse (YYYY-MM-DD)", example="2021-01-01"),
    end_date: date = Query(..., description="Date de fin de l'analyse (YYYY-MM-DD)", example="2023-12-31"),
):
    """
    Cet endpoint permet de calculer la somme pondérée des poids des objets trouvés,
    en fonction de la couverture nuageuse et des heures d'ensoleillement pendant une période donnée.

    L'utilisateur doit fournir :
    - Le seuil de couverture nuageuse (cloud) [entre 0 et 100].
    - Les heures d'ensoleillement (sun) [heures de soleil par jour].
    - Une plage de dates (start_date, end_date) pour laquelle l'analyse doit être effectuée.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        SELECT AVG(o.poids_pondere) AS somme_poids_pondere
        FROM objets_trouves o
        INNER JOIN lumiere l ON o.date = l.date
        WHERE l.cloud > ? AND l.sun > ? AND o.date BETWEEN ? AND ?
    """
    
    cursor.execute(query, (cloud, sun, start_date, end_date))  # Exécution de la requête
    result = cursor.fetchone()

    cursor.close()  # Fermeture du curseur et de la connexion
    connection.close()

    if result:
        return LumiereWithPoidsResponse(somme_poids_pondere=result[0])  # Vérification du résultat et retour de la réponse
    else:
        raise HTTPException(status_code=404, detail="Aucune donnée trouvée correspondant aux critères.")