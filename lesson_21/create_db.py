from lesson_21.database import engine
from lesson_21.model import Base
from sqlalchemy import inspect
from sqlalchemy import text

Base.metadata.create_all(engine)

inspector = inspect(engine)
print(inspector.get_table_names())

with engine.connect() as conn:
    print(conn.execute(text("SELECT current_database();")).fetchone())