
import requests
import logging
from datetime import datetime
from dateparser import parse  #pr parser au format date
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from .model import LostItem, Temperature, Gare
from typing import List, Tuple
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from abc import ABCMeta, abstractmethod # permet de définir des classes de base


logging.basicConfig(level=logging.INFO)

class Importer(metaclass = ABCMeta):

def __init__(self, engine: Engine):
    self.engine = engine
    #je vais instancier ts mes importer avec un engine (b qui est une connection à une bdd
    #engine: pointage vers la database
    #sessionmaker: va la conecter

    self.Session = sessionmaker(bind=engine)
    self.session = self.Session()
    self._init_attributes()
    #méthode appelée dés l'initialisation (tt ce qi est ds l'init: appelé ds l'instanciation)
# ttes les classes filles héritent de init, mais pr init_attributes(), ca va ds l'init des enfants, mais aura un init différent!

#rappel, qd hérite: super.__init__(engine): on rappelle tt l'init de la mère: pr compéter par l'init perso de fille
@abstractmethod   #on l'a mis là pr pas surcharger init
#décorateur: fction qui prend en entrée une fction: et qui retourne une autre fonction
#ca va venir modifier votre fction  / méthode qu'on utilise ds classe abstraite, et que classes filles sont obligées de redéfinir
def _init_attributes(self):
    self.TableModel = None
    self.field_list = None

#parfois la classe qui hérite va surcharger la méthode init ou autre(redéfinir une méthode déjà héritée)
def _parse_date(self, start_date: str, end_date: str) -> Tuple[datetime, datetime]:
    #classe qui commence par "_">> encapsulation: mettre méthodes inside class: pr dire méthode peut etre use ds classe mais aps en dehors de la  classe
    #on va pas se servir de cette méthode ouvertement (juste à l'intérieur d'une autre classe
    # #python va pas ns bloquer >>> mais convention entre dvlopeurs)= méthodes protégées
    #on comprend D quelles sont les vraies méthodes
    #__(double underscore): méthodes privées: pas appelable du tt: ne s'héritent pas d'une classe à l'autre
    start_parse = parse(str(start_date))   #use fction parse, importée au début!
    end_parse = parse(str(end_date))
    return start_parse, end_parse
#prend une date et la remet au format datetime
#donne date de début et de fin, pr pouvoir éventuellement update


def _get_year_range(self, start_date: str, end_date: str) -> List[Tuple[str, str]]:
    year_ranges = []
    #va prendre du 1/6/20 au 31/12/20 + 1/1/21-31/12/21
    start_parse, end_parse = self._parse_date(start_date,end_date)
    current_year = start_parse.year

    while current_year <= end_parse.year:
        year_start = datetime(current_year, 1, 1,1,1,1)#= 1ÉRE HEURE 1ER JANVIER
        year_end = datetime(current_year, 12, 31,23,59,59)#DERNIÉRE HEURE 31/12/23

    if current_year == start_parse.year:
        year_start = start_parse
    if current_year == end_parse.year:
        year_end = end_parse

    year_ranges.append((str(year_start.date()), str(year_end.date())))
    current_year += 1
    return year_ranges


def clean(self) -> None:
    self.session.query(self.TableModel).delete()#je delete tt le contenu de la table de donnée(pas la table)
    # self.session.query(LostItem).delete()
    self.session.commit()

@abstractmethod
def import_data(self,x,y):
    #va me permettre d'importer entre 2 dates/ ttes mes filles en ont besoin
    pass

@abstractmethod
def _create_endpoint(self):
    #créer endpoint pr requeter les api
    pass

def _get_last_date(self) -> str:
    #prend la dernière date de ma BDD!
    date_string = self.session.query(func.max(LostItem.date)).scalar()
    #je vais chercher le max de la colonne date de lostitem (pr voir dernière date importée ds lostitem)
    return str(datetime.fromisoformat(date_string).date())
#fromisoformat: format de date

def update(self)-> None:
    self.import_data(self. _get_last_date(),"now")
#va me permettre d'importer data entre date de debut et date de fin


def _insert(self, my_request: requests.Response) -> None:
    #pr chaque ligne de ce que j'ai récup, crée un dico, je rajoute = code d'insertion pr ttes les tables
    for row in my_request.json()["records"]:
        row_data = {} 
    for field in self.field_list:
        try: 
            row_data[field[0]] = row["fields"][field[1]]
        except KeyError:
            row_data[field[0]] = None

# self.session.add(LostItem(**temp_data))
            self.session.add(self.TableModel(**row_data))
        self.session.commit()


#classe filles vont mettre leurs différences
class LostItemImporter(Importer):

station_list = ["Paris Austerlitz", "Paris Est", "Paris Gare de Lyon", "Paris Gare du Nord", "Paris Montparnasse", "Paris Saint-Lazare", "Paris Bercy"]

def _init_attributes(self):
self.TableModel= LostItem
self.field_list = [
["date", "date"],
["type_objet", "gc_obo_type_c"],
["nom_gare", "gc_obo_gare_origine_r_name"],
["date_restitution", "gc_obo_date_heure_restitution_c"],
]
#ce qui est spécifique à la fille: l'url, les dates etc
def _create_endpoint(self, station: str, start: str, end: str) -> str:
URL = "https://ressources.data.sncf.com/api/records/1.0/search/"
ressource = "?dataset=objets-trouves-restitution&q="
date_fork = f"date%3A%5B{start}+TO+{end}%5D"
row_limit ="&rows=10000"
station = f"&refine.gc_obo_gare_origine_r_name={station}"
endpoint = URL + ressource + date_fork + row_limit + station
return endpoint.replace(" ", "+")


def import_data(self, start_date: str, end_date: str) -> None:
# Set up logging

    year_range = self._get_year_range(start_date,end_date)

    for station in self.station_list:
        for start_date, end_date in year_range:

            my_request = requests.get(self._create_endpoint(station, start_date, end_date))

            logging.info(f"REQUETE: {start_date}, {station},{len((my_request.json()['records']))}")
#sert à voir ce qui se passe
#OO cout d'architecture au départ: gain à la lecture
#permet flexibilité, pr changer un bout sans impact
            self._insert(my_request)

class TemperatureImporter(Importer):


def _init_attributes(self):
self.TableModel= Temperature
self.field_list = [
["date", "date"],
["temperature", "tc"],
]

def _create_endpoint(self, start: str, end: str) -> str:
URL = "https://public.opendatasoft.com/api/records/1.0/search/"
ressource = "?dataset=donnees-synop-essentielles-omm&q="
date_fork = f"date%3A%5B{start}+TO+{end}%5D"
row_limit ="&rows=10000"
station = f"&refine.nom=ORLY"
endpoint = URL + ressource + date_fork + row_limit +station
return endpoint.replace(" ", "+")

def import_data(self, start_date: str, end_date: str) -> None:
# Set up logging

year_range = self._get_year_range(start_date,end_date)

for start_date, end_date in year_range:

my_request = requests.get(self._create_endpoint(start_date, end_date))

logging.info(f"REQUETE: {start_date},{len((my_request.json()['records']))}")

self._insert(my_request)


class GareImporter(Importer):

station_list = ["Paris Austerlitz", "Paris Est", "Paris Gare de Lyon", "Paris Gare du Nord", "Paris Montparnasse", "Paris Saint-Lazare", "Paris Bercy"]

def _init_attributes(self):
self.TableModel= Gare
self.field_list = [
["latitude", "latitude_entreeprincipale_wgs84"],
["longitude", "longitude_entreeprincipale_wgs84"],
]

def _create_endpoint(self,station:str)->Tuple[str,str]:
URL_geo = "https://ressources.data.sncf.com/api/records/1.0/search/"
ressource_geo = "?dataset=referentiel-gares-voyageurs"
row_limit_geo ="&rows=1"
stationt_geo = f"&refine.gare_alias_libelle_noncontraint={station}"
endpoint_gare = URL_geo + ressource_geo + row_limit_geo + stationt_geo


URL_freq = "https://ressources.data.sncf.com/api/records/1.0/search/"
ressource_freq = "?dataset=frequentation-gares"
row_limit_freq ="&rows=1"
station_freq = f"&refine.nom_gare={station}"
endpoint_freq = URL_freq + ressource_freq + row_limit_freq + station_freq

return (endpoint_gare,endpoint_freq)


def import_data(self):

for station in self.station_list:
if station == "Paris Bercy":
station_lib = "Paris Bercy Bourgogne - Pays d'Auvergne"

else:
station_lib = station

my_request_geo = requests.get(self._create_endpoint(station_lib)[0])
my_request_freq = requests.get(self._create_endpoint(station_lib)[1])

logging.info(f"REQUETE: {station}")

self._insert(my_request_geo, my_request_freq, station)

def _insert(self, my_request_geo: requests.Response, my_request_freq: requests.Response, station:str) -> None:

geo_data = my_request_geo.json()["records"][0] # Only one row is collected for each station 
row_data = {} 
for field in self.field_list:
try: 
row_data[field[0]] = geo_data["fields"][field[1]]
except KeyError:
row_data[field[0]] = None

freq_data = my_request_freq.json()["records"][0]
row_data["freq_2019"] = freq_data["fields"]["total_voyageurs_non_voyageurs_2019"]+freq_data["fields"]["total_voyageurs_2019"]
row_data["freq_2020"] = freq_data["fields"]["total_voyageurs_non_voyageurs_2020"]+freq_data["fields"]["total_voyageurs_2020"]
row_data["freq_2021"] = freq_data["fields"]["total_voyageurs_non_voyageurs_2021"]+freq_data["fields"]["total_voyageurs_2021"]

# self.session.add(LostItem(**temp_data))
self.session.add(Gare(nom_gare=station,**row_data))
self.session.commit()


if __name__ == "__main__":
engine = create_engine('sqlite:///db.sqlite')
my_import = LostItemImporter(engine)
my_import.clean()
