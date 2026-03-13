from fastapi import FastAPI
from app.core.database import Base, engine
from app.features.tasks.routes import router as tasks_router
from app.features.home.routes import router as home_router
 
# Create tables (run once at startup)
Base.metadata.create_all(bind=engine)
 
# Initialize FastAPI
app = FastAPI()
 
# Include task routes
app.include_router(tasks_router)

# Include home route
app.include_router(home_router)

