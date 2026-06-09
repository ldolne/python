from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session
from dotenv import load_dotenv
import os

from models import Base ## Quand on utilise le __init__
load_dotenv()

url = os.getenv('DB_URL')
engine = create_engine(url=url)

Base.metadata.create_all(bind=engine) # permet de récupérer toutes les classes qui héritent de Base et de les créer en DB via l'engine (ne les crée qu'une fois, donc peut être relancé)

# with create_session(bind=engine) as session: # pour couper connexion DB à la sortie du with
#     stmt = text('SELECT * FROM person')
#     rows = session.execute(stmt).all()

#     for s in rows:
#         print(s)