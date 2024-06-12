# main.py

from fastapi import FastAPI
from app.api.endpoints import configurations
from app.database import engine, create_tables

app = FastAPI()

# Create tables on application startup
create_tables()

# Include API routers
app.include_router(configurations.router, prefix="/api/v1", tags=["configurations"])
