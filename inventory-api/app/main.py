from fastapi import FastAPI
from app.routes import inventory

app = FastAPI()

app.include_router(inventory.router)

@app.get("/")
def read_root():
    return {"message": "Inventory API is running"}