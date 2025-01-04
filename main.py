from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!", "app_name": settings.app_name, "admin_email": settings.admin_email}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
