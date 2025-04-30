from fastapi import FastAPI
from app.routes import inventory
from routes import inventory
from database.connection import engine
from models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(inventory.router)

# @app.get("/")
# def read_root():
#     return {"message": "Inventory API is running"}