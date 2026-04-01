from gettext import find

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = """postgresql+psycopg2://neondb_owner:npg_zuwhtvq0MCk4@ep-morning-wind-amck762s-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"""

engine = create_engine(DATABASE_URL)

session = sessionmaker(bind=engine)

def get_db():
    with session() as db:
        yield db

db_gen = get_db()
db = next(db_gen)