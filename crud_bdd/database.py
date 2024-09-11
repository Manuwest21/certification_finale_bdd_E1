from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Remplacez les valeurs entre crochets par vos informations Azure SQL
DATABASE_URL = (
    "mssql+pyodbc://manu21:*Servor1@rg-devries-serveur.database.windows.net/luminosite-devries?"
    "driver=ODBC+Driver+18+for+SQL+Server"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()