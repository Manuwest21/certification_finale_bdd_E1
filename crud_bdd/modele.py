from sqlalchemy import Column, Integer, String, Date
from database import Base

class Lumiere(Base):
    __tablename__ = "lumiere"

    date = Column(Date, primary_key=True)
    cloud = Column(String(255), nullable=False)
    sun = Column(String(255), nullable=False)

class ObjetsTrouves(Base):
    __tablename__ = "objets_trouves"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    type = Column(String(255), nullable=False)
    gare = Column(String(255), nullable=False)

class Frequentation(Base):
    __tablename__ = "frequentation"

    gare = Column(String, primary_key=True)
    frequent_2021 = Column(Integer, nullable=False)
    frequent_2022 = Column(Integer, nullable=False)
    frequent_2023 = Column(Integer, nullable=False)
