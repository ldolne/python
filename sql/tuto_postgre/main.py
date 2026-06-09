from models import Base # Quand on utilise le __init__

# with create_session(bind=engine) as session: # pour couper connexion DB à la sortie du with
#     stmt = text('SELECT * FROM person')
#     rows = session.execute(stmt).all()

#     for s in rows:
#         print(s)