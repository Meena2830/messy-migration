from app.db import Base, engine
from app import models

print("Initializing the database...")
Base.metadata.create_all(bind=engine)
print("Database initialized.")
