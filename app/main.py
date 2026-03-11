from fastapi import FastAPI
from app.core.database import Base, engine

# Create tables (run once at startup)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()



