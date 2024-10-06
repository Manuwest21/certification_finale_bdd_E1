from sqlalchemy.orm import Session
import modele, schema
from typing import List

# CRUD operations for Lumiere
def create_lumiere(db: Session, lumiere: schema.LumiereCreate):
    db_lumiere = modele.Lumiere(date=lumiere.date, cloud=lumiere.cloud, sun=lumiere.sun)
    db.add(db_lumiere)
    db.commit()
    db.refresh(db_lumiere)
    return db_lumiere

def get_lumiere(db: Session, date: str):
    return db.query(modele.Lumiere).filter(modele.Lumiere.date == date).first()

def get_all_lumieres(db: Session, skip: int = 0, limit: int = 10) -> List[modele.Lumiere]:
    return db.query(modele.Lumiere).offset(skip).limit(limit).all()

def update_lumiere(db: Session, date: str, lumiere_update: schema.LumiereCreate):
    db_lumiere = db.query(modele.Lumiere).filter(modele.Lumiere.date == date).first()
    if db_lumiere:
        db_lumiere.cloud = lumiere_update.cloud
        db_lumiere.sun = lumiere_update.sun
        db.commit()
        db.refresh(db_lumiere)
    return db_lumiere

def delete_lumiere(db: Session, date: str):
    db_lumiere = db.query(modele.Lumiere).filter(modele.Lumiere.date == date).first()
    if db_lumiere:
        db.delete(db_lumiere)
        db.commit()
    return db_lumiere

# CRUD operations for ObjetsTrouves
def create_objets_trouves(db: Session, objets_trouves: schema.ObjetsTrouvesCreate):
    db_objets_trouves = modele.ObjetsTrouves(date=objets_trouves.date, type=objets_trouves.type, gare=objets_trouves.gare)
    db.add(db_objets_trouves)
    db.commit()
    db.refresh(db_objets_trouves)
    return db_objets_trouves

def get_objets_trouves(db: Session, id: int):
    return (
        db.query(modele.ObjetsTrouves)
        .filter(modele.ObjetsTrouves.id == id)
        .order_by(modele.ObjetsTrouves.id)  
        .first()
      )

def get_all_objets_trouves(db: Session, skip: int = 0, limit: int = 10) -> List[modele.ObjetsTrouves]:
      return (
        db.query(modele.ObjetsTrouves)
        .order_by(modele.ObjetsTrouves.id)  
        .offset(skip)
        .limit(limit)
        .all()
     )

def update_objets_trouves(db: Session, id: int, objets_trouves_update: schema.ObjetsTrouvesCreate):
    db_objets_trouves = db.query(modele.ObjetsTrouves).filter(modele.ObjetsTrouves.id == id).first()
    if db_objets_trouves:
        db_objets_trouves.date = objets_trouves_update.date
        db_objets_trouves.type = objets_trouves_update.type
        db_objets_trouves.gare = objets_trouves_update.gare
        db.commit()
        db.refresh(db_objets_trouves)
    return db_objets_trouves

def delete_objets_trouves(db: Session, id: int):
    db_objets_trouves = db.query(modele.ObjetsTrouves).filter(modele.ObjetsTrouves.id == id).first()
    if db_objets_trouves:
        db.delete(db_objets_trouves)
        db.commit()
    return db_objets_trouves

# CRUD operations for Frequentation
def create_frequentation(db: Session, frequentation: schema.FrequentationCreate):
    db_frequentation = modele.Frequentation(
        gare=frequentation.gare,
        frequent_2021=frequentation.frequent_2021,
        frequent_2022=frequentation.frequent_2022,
        frequent_2023=frequentation.frequent_2023
    )
    db.add(db_frequentation)
    db.commit()
    db.refresh(db_frequentation)
    return db_frequentation

def get_frequentation(db: Session, gare: str):
    return db.query(modele.Frequentation).filter(modele.Frequentation.gare == gare).first()

def get_all_frequentations(db: Session, skip: int = 0, limit: int = 10) -> List[modele.Frequentation]:
    return db.query(modele.Frequentation).offset(skip).limit(limit).all()

def update_frequentation(db: Session, gare: str, frequentation_update: schema.FrequentationCreate):
    db_frequentation = db.query(modele.Frequentation).filter(modele.Frequentation.gare == gare).first()
    if db_frequentation:
        db_frequentation.frequent_2021 = frequentation_update.frequent_2021
        db_frequentation.frequent_2022 = frequentation_update.frequent_2022
        db_frequentation.frequent_2023 = frequentation_update.frequent_2023
        db.commit()
        db.refresh(db_frequentation)
    return db_frequentation

def delete_frequentation(db: Session, gare: str):
    db_frequentation = db.query(modele.Frequentation).filter(modele.Frequentation.gare == gare).first()
    if db_frequentation:
        db.delete(db_frequentation)
        db.commit()
    return db_frequentation


