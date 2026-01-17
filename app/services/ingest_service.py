from core.database import SessionLocal, neo4j_driver
from models.postgres import User

def ingest_user(data: dict):
    db = SessionLocal()

    # PostgreSQL
    user = db.query(User).filter_by(user_id=data["user_id"]).first()
    if user:
        user.name = data["name"]
        user.email = data["email"]
    else:
        user = User(**data)
        db.add(user)

    db.commit()

    # Neo4j
    with neo4j_driver.session() as session:
        session.run(
            """
            MERGE (u:User {user_id: $user_id})
            SET u.name = $name, u.email = $email
            """,
            **data
        )
