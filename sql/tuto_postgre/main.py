from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models import Base, init_db, get_db_session, engine # Quand on utilise le __init__
from models import Category
from models import Plant
from models import Customer
from models import Order, OrderLine
# with create_session(bind=engine) as session: # pour couper connexion DB à la sortie du with
#     stmt = text('SELECT * FROM person')
#     rows = session.execute(stmt).all()

#     for s in rows:
#         print(s)

def create_sample_data(session): # prend la session en argument pour faire différents traitements au fur et à mesure
    # Création de catégories
    flower_category = Category(name="Flower") # MappedAsDataclass force le typage de nos modèles
    interior_category = Category(name="Plante d'intérieur")
    exterior_category = Category(name="Plante d'extérieur") 

    session.add_all([flower_category, interior_category, exterior_category])

    session.flush() # Envoie à la db sans commit définitif (le but est d'ici avoir les ids)
    print("Catégories créées et flush... (avoir les ids)")

    # Créer des plantes avec relation Many-to-Many
    rose = Plant(name="Rose rouge",
                description="Belle rose rouge",
                base_price=Decimal("4.50"),
                categories=[flower_category, interior_category] # assignation directe => jointure N-M automatique
            )
    jonquille = Plant(name="Jonquille",
                description="Jolie jonquille jaune",
                base_price=Decimal("1.45"),
                categories=[flower_category, exterior_category]
            )
    ficus = Plant(name="Ficus",
                description="Beau ficus",
                base_price=Decimal("1.80"),
                categories=[flower_category, interior_category]
            )
    session.add_all([rose, jonquille, ficus])
    session.add(rose)
    session.flush()

    print("Plantes créées avec leurs catégories et flush... (table associative bien remplie)")

    customer = Customer(
        first_name="Mike",
        last_name="Marino",
    )

    session.add(customer)
    session.flush()

    print(f"Customer: {customer.first_name} {customer.id}")

    # Utilisation de la méthode métier
    order = customer.place_order(session, [(rose,3), (jonquille, 10), (ficus,1)])

    print("Commandes créées automatiquement:", order.id)

    session.commit()

def demonstrate_loading_join(session):
    # LAZY
    customer = session.execute(
            select(Customer).where(Customer.last_name == "Marino")
        ).scalar_one_or_none()
    
    if customer:
        print("Client trouvé", customer.last_name)
        print(f"Orders number: {len(customer.orders)} (requête en lazy)")

        for order in customer.orders:
            print(f"Order #{order.id} | Total: {order.total():.2f} €")

    # EAGER | selectinload()
    stmt = (
        select(Customer)
        .options(
            #on dit à Alchemy de charger aussi les tables jointes
            selectinload(Customer.orders).selectinload(Order.order_lines).selectinload(OrderLine.plant)
        ).where(Customer.last_name == "Marino")
    )

    customer = session.execute(stmt).scalar_one_or_none()
    
    if customer:
        for order in customer.orders:
            print(f"Order #{order.id} | Total: {order.total():.2f} €")
            for line in order.order_lines:
                print(f"- {line.quantity} x {line.plant.name} = {line.line_total():.2f} €")

    # Query like SQL
    stmt = (
        select(Plant)
        .join(Plant.categories)
        .where(Category.name == "Flower")
        .order_by(Plant.name)
    )

    plant_flowers = session.execute(stmt).scalars().all() # to get all lines

    for p in plant_flowers:
        print(f"- Plant flower {p.name}")

    # Pure SQL is possible too with text("SELECT * FROM customer")

if __name__ == "__main__":
    with get_db_session() as session:

        init_db(delete=True)
        # init_db()

        # vérification pour voir si nos données existent déjà
        existing_customer = session.execute(select(Customer)).scalar_one_or_none() # retourne un scalaire ou rien si rien trouvé

        if not existing_customer:
            create_sample_data(session)
            demonstrate_loading_join(session)
        else:
            print("Données déjà présentes")