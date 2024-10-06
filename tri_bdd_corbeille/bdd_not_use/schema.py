from pydantic import BaseModel
from typing import Optional

# Schémas pour la table Lumiere
class LumiereCreate(BaseModel):
    date: str  # ISO format for date (YYYY-MM-DD)
    cloud: str
    sun: str

class LumiereResponse(BaseModel):
    date: str
    cloud: str
    sun: str

    class Config:
        from_attributes = True

# Schémas pour la table ObjetsTrouves
class ObjetsTrouvesCreate(BaseModel):
    date: str  # ISO format for date (YYYY-MM-DD)
    type: str
    gare: str

class ObjetsTrouvesResponse(BaseModel):
    id: int
    date: str
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
