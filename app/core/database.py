from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from neo4j import GraphDatabase

engine = create_engine(settings.postgres_dsn)
SessionLocal = sessionmaker(bind=engine)

neo4j_driver = GraphDatabase.driver(
    settings.neo4j_uri,
    auth=(settings.neo4j_user, settings.neo4j_password)
)
