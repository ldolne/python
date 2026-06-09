from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class Base(MappedAsDataclass, DeclarativeBase):
    pass

load_dotenv()

url = os.getenv('DB_URL')
engine = create_engine(url=url)
Base.metadata.create_all(bind=engine) # permet de récupérer toutes les classes qui héritent de Base et de les créer en DB via l'engine (ne les crée qu'une fois, donc peut être relancé)
