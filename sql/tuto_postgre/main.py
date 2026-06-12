from models.base import Base, init_db, get_db_session, engine # Quand on utilise le __init__

# with create_session(bind=engine) as session: # pour couper connexion DB à la sortie du with
#     stmt = text('SELECT * FROM person')
#     rows = session.execute(stmt).all()

#     for s in rows:
#         print(s)

if __name__ == "__main__":
    init_db()