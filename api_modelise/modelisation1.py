import pyodbc
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import date
from fastapi.routing import APIRouter

app = APIRouter()
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

# Schémas Pydantic
class LumiereCreate(BaseModel):
    date: date
    cloud: str
    sun: str

class LumiereResponse(BaseModel):
    date: date
    cloud: str
    sun: str

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
    gare: str
    frequent_2021: int
    frequent_2022: int
    frequent_2023: int

class FrequentationResponse(BaseModel):
    gare: str
    frequent_2021: int
    frequent_2022: int
    frequent_2023: int



class LumiereWithPoidsCreate(BaseModel):
    start_date: date
    end_date: date
    cloud: int
    sun: int

class LumiereWithPoidsResponse(BaseModel):
    somme_poids_pondere: float

# CRUD Operations for Lumiere

@app.post("/lumiere/", response_model=LumiereResponse)
def create_lumiere(lumiere: LumiereCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO lumiere (date, cloud, sun)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, lumiere.date, lumiere.cloud, lumiere.sun)
    connection.commit()
    cursor.close()
    connection.close()
    return lumiere

@app.get("/lumiere/{date}", response_model=LumiereResponse)
def read_lumiere(date: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT date, cloud, sun FROM lumiere WHERE date = ?"
    cursor.execute(query, date)
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    if row:
        return {"date": row[0], "cloud": row[1], "sun": row[2]}
    else:
        raise HTTPException(status_code=404, detail="Lumiere not found")

@app.get("/lumiere/", response_model=List[LumiereResponse])
def read_lumieres(skip: int = 0, limit: int = 10):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT date, cloud, sun FROM lumiere ORDER BY date OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
    cursor.execute(query, skip, limit)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{"date": row[0], "cloud": row[1], "sun": row[2]} for row in rows]

@app.put("/lumiere/{date}", response_model=LumiereResponse)
def update_lumiere(date: str, lumiere_update: LumiereCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        UPDATE lumiere SET cloud = ?, sun = ?
        WHERE date = ?
    """
    cursor.execute(query, lumiere_update.cloud, lumiere_update.sun, date)
    connection.commit()
    cursor.close()
    connection.close()
    return lumiere_update

@app.delete("/lumiere/{date}", response_model=LumiereResponse)
def delete_lumiere(date: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM lumiere WHERE date = ?"
    cursor.execute(query, date)
    connection.commit()
    cursor.close()
    connection.close()
    return {"date": date}

# CRUD Operations for ObjetsTrouves

@app.post("/objets_trouves/", response_model=ObjetsTrouvesResponse)
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

@app.get("/objets_trouves/{id}", response_model=ObjetsTrouvesResponse)
def read_objets_trouves(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT id, date, type, gare FROM objets_trouves WHERE id = ?"
    cursor.execute(query, id)
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    if row:
        return {"id": row[0], "date": row[1], "type": row[2], "gare": row[3]}
    else:
        raise HTTPException(status_code=404, detail="Objets Trouves not found")

@app.get("/objets_trouves/", response_model=List[ObjetsTrouvesResponse])
def read_objets_trouves_list(skip: int = 0, limit: int = 10):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT id, date, type, gare FROM objets_trouves ORDER BY date OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
    cursor.execute(query, skip, limit)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{"id": row[0], "date": row[1], "type": row[2], "gare": row[3]} for row in rows]

@app.put("/objets_trouves/{id}", response_model=ObjetsTrouvesResponse)
def update_objets_trouves(id: int, objets_trouves_update: ObjetsTrouvesCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        UPDATE objets_trouves SET date = ?, type = ?, gare = ?
        WHERE id = ?
    """
    cursor.execute(query, objets_trouves_update.date, objets_trouves_update.type, objets_trouves_update.gare, id)
    connection.commit()
    cursor.close()
    connection.close()
    return objets_trouves_update

@app.delete("/objets_trouves/{id}", response_model=ObjetsTrouvesResponse)
def delete_objets_trouves(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM objets_trouves WHERE id = ?"
    cursor.execute(query, id)
    connection.commit()
    cursor.close()
    connection.close()
    return {"id": id}

# CRUD Operations for Frequentation

@app.post("/frequentation/", response_model=FrequentationResponse)
def create_frequentation(frequentation: FrequentationCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO frequentation (gare, frequent_2021, frequent_2022, frequent_2023)
        VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, frequentation.gare, frequentation.frequent_2021, frequentation.frequent_2022, frequentation.frequent_2023)
    connection.commit()
    cursor.close()
    connection.close()
    return frequentation

@app.get("/frequentation/{gare}", response_model=FrequentationResponse)
def read_frequentation(gare: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT gare, frequent_2021, frequent_2022, frequent_2023 FROM frequentation WHERE gare = ?"
    cursor.execute(query, gare)
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    if row:
        return {"gare": row[0], "frequent_2021": row[1], "frequent_2022": row[2], "frequent_2023": row[3]}
    else:
        raise HTTPException(status_code=404, detail="Frequentation not found")

@app.get("/frequentation/", response_model=List[FrequentationResponse])
def read_frequentations(skip: int = 0, limit: int = 10):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT gare, frequent_2021, frequent_2022, frequent_2023 FROM frequentation ORDER BY gare OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
    cursor.execute(query, skip, limit)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{"gare": row[0], "frequent_2021": row[1], "frequent_2022": row[2], "frequent_2023": row[3]} for row in rows]

@app.put("/frequentation/{gare}", response_model=FrequentationResponse)
def update_frequentation(gare: str, frequentation_update: FrequentationCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        UPDATE frequentation SET frequent_2021 = ?, frequent_2022 = ?, frequent_2023 = ?
        WHERE gare = ?
    """
    cursor.execute(query, frequentation_update.frequent_2021, frequentation_update.frequent_2022, frequentation_update.frequent_2023, gare)
    connection.commit()
    cursor.close()
    connection.close()
    return frequentation_update

@app.delete("/frequentation/{gare}", response_model=FrequentationResponse)
def delete_frequentation(gare: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM frequentation WHERE gare = ?"
    cursor.execute(query, gare)
    connection.commit()
    cursor.close()
    connection.close()
    return {"gare": gare}


@app.post("/cloud_sun/", response_model=LumiereWithPoidsResponse)
def calculate_poids_pondere(lumiere: LumiereWithPoidsCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
        SELECT AVG(o.poids_pondere) AS somme_poids_pondere
        FROM objets_trouves9 o
        INNER JOIN lumiere9 l ON o.date = l.date
        WHERE l.cloud < ? AND l.sun > ? AND o.date BETWEEN ? AND ?
    """
    
    cursor.execute(query, (lumiere.cloud, lumiere.sun, lumiere.start_date, lumiere.end_date))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if result:
        return LumiereWithPoidsResponse(somme_poids_pondere=result[0])
    else:
        raise HTTPException(status_code=404, detail="No data found matching criteria")
