from contextlib import contextmanager

from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class Base(DeclarativeBase): # MappedAsDataclass commenté pour l'instant
    pass

load_dotenv()

url = os.getenv('DB_URL')
engine = create_engine(url=url,echo=True) # Echo donne plein de détails de logs
# Base.metadata.create_all(bind=engine) # permet de récupérer toutes les classes qui héritent de Base et de les créer en DB via l'engine (ne les crée qu'une fois, donc peut être relancé)

session_local = sessionmaker(
    autocommit=False,  # désactive le commit automatique : quand on veut enregistrer qqch en db, c'est nous qui le choisissons
    autoflush=False, # permet de valider les éléments en local (ex. commit local sans pusher sur distant)
    bind=engine, # le moteur créé va être bindé sur notre session
    expire_on_commit=False # attention avec dataclass
)

def init_db(delete=False):
    if(delete):
        Base.metadata.drop_all(bind=engine)
        print("[INFOS] : Table deleted")
    Base.metadata.create_all(bind=engine)
    print("[INFOS] : Table created")

@contextmanager # permet d'identifier ce qui va se passer sur les routes qui mènent à la db, permet de gérer sessions proprement
def get_db_session():
    session = session_local()
    try:
        yield session
        session.commit() # commit si pas d'erreur dans l'exécution DB
    except Exception:
        session.rollback() # rollback la transaction courante
    finally:
        session.close()