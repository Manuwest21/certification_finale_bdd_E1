from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import schema, crud, modele

app = FastAPI()

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Lumiere
@app.post("/lumiere/", response_model=schema.LumiereResponse)
def create_lumiere(lumiere: schema.LumiereCreate, db: Session = Depends(get_db)):
    return crud.create_lumiere(db=db, lumiere=lumiere)

@app.get("/lumiere/{date}", response_model=schema.LumiereResponse)
def read_lumiere(date: str, db: Session = Depends(get_db)):
    db_lumiere = crud.get_lumiere(db, date=date)
    if db_lumiere is None:
        raise HTTPException(status_code=404, detail="Lumiere not found")
    return db_lumiere

@app.get("/lumiere/", response_model=list[schema.LumiereResponse])
def read_lumieres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    lumieres = crud.get_all_lumieres(db, skip=skip, limit=limit)
    return lumieres

@app.put("/lumiere/{date}", response_model=schema.LumiereResponse)
def update_lumiere(date: str, lumiere_update: schema.LumiereCreate, db: Session = Depends(get_db)):
    updated_lumiere = crud.update_lumiere(db=db, date=date, lumiere_update=lumiere_update)
    if updated_lumiere is None:
        raise HTTPException(status_code=404, detail="Lumiere not found")
    return updated_lumiere

@app.delete("/lumiere/{date}", response_model=schema.LumiereResponse)
def delete_lumiere(date: str, db: Session = Depends(get_db)):
    deleted_lumiere = crud.delete_lumiere(db=db, date=date)
    if deleted_lumiere is None:
        raise HTTPException(status_code=404, detail="Lumiere not found")
    return deleted_lumiere

# CRUD operations for ObjetsTrouves
@app.post("/objets_trouves/", response_model=schema.ObjetsTrouvesResponse)
def create_objets_trouves(objets_trouves: schema.ObjetsTrouvesCreate, db: Session = Depends(get_db)):
    return crud.create_objets_trouves(db=db, objets_trouves=objets_trouves)

@app.get("/objets_trouves/{id}", response_model=schema.ObjetsTrouvesResponse)
def read_objets_trouves(id: int, db: Session = Depends(get_db)):
    db_objets_trouves = crud.get_objets_trouves(db, id=id)
    if db_objets_trouves is None:
        raise HTTPException(status_code=404, detail="ObjetsTrouves not found")
    return db_objets_trouves

@app.get("/objets_trouves/", response_model=list[schema.ObjetsTrouvesResponse])
def read_objets_trouves_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    objets_trouves = crud.get_all_objets_trouves(db, skip=skip, limit=limit)
    return objets_trouves

@app.put("/objets_trouves/{id}", response_model=schema.ObjetsTrouvesResponse)
def update_objets_trouves(id: int, objets_trouves_update: schema.ObjetsTrouvesCreate, db: Session = Depends(get_db)):
    updated_objets_trouves = crud.update_objets_trouves(db=db, id=id, objets_trouves_update=objets_trouves_update)
    if updated_objets_trouves is None:
        raise HTTPException(status_code=404, detail="ObjetsTrouves not found")
    return updated_objets_trouves

@app.delete("/objets_trouves/{id}", response_model=schema.ObjetsTrouvesResponse)
def delete_objets_trouves(id: int, db: Session = Depends(get_db)):
    deleted_objets_trouves = crud.delete_objets_trouves(db=db, id=id)
    if deleted_objets_trouves is None:
        raise HTTPException(status_code=404, detail="ObjetsTrouves not found")
    return deleted_objets_trouves

# CRUD operations for Frequentation
@app.post("/frequentation/", response_model=schema.FrequentationResponse)
def create_frequentation(frequentation: schema.FrequentationCreate, db: Session = Depends(get_db)):
    return crud.create_frequentation(db=db, frequentation=frequentation)

@app.get("/frequentation/{gare}", response_model=schema.FrequentationResponse)
def read_frequentation(gare: str, db: Session = Depends(get_db)):
    db_frequentation = crud.get_frequentation(db, gare=gare)
    if db_frequentation is None:
        raise HTTPException(status_code=404, detail="Frequentation not found")
    return db_frequentation

@app.get("/frequentation/", response_model=list[schema.FrequentationResponse])
def read_frequentations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    frequentations = crud.get_all_frequentations(db, skip=skip, limit=limit)
    return frequentations

@app.put("/frequentation/{gare}", response_model=schema.FrequentationResponse)
def update_frequentation(gare: str, frequentation_update: schema.FrequentationCreate, db: Session = Depends(get_db)):
    updated_frequentation = crud.update_frequentation(db=db, gare=gare, frequentation_update=frequentation_update)
    if updated_frequentation is None:
        raise HTTPException(status_code=404, detail="Frequentation not found")
    return updated_frequentation

@app.delete("/frequentation/{gare}", response_model=schema.FrequentationResponse)
def delete_frequentation(gare: str, db: Session = Depends(get_db)):
    deleted_frequentation = crud.delete_frequentation(db=db, gare=gare)
    if deleted_frequentation is None:
        raise HTTPException(status_code=404, detail="Frequentation not found")
    return deleted_frequentation
