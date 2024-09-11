from pydantic import BaseModel
from typing import Optional
from datetime import date
# Schémas pour la table Lumiere
class LumiereCreate(BaseModel):
    date: date  # ISO format for date (YYYY-MM-DD)
    cloud: str
    sun: str

class LumiereResponse(BaseModel):
    date: date
    cloud: str
    sun: str

    class Config:
        from_attributes = True

# Schémas pour la table ObjetsTrouves
class ObjetsTrouvesCreate(BaseModel):
    date: date  # ISO format for date (YYYY-MM-DD)
    type: str
    gare: str

   

class ObjetsTrouvesResponse(BaseModel):
    id: int
    date: date
    type: str
    gare: str

    class Config:
        from_attributes = True

# Schémas pour la table Frequentation
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

    class Config:
        from_attributes = True
