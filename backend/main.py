import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models.item as models
from database import engine, SessionLocal, Base

app = FastAPI()

# ================= CORS FIX =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend to talk to backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ CREATE DATABASE TABLES ============
Base.metadata.create_all(bind=engine)

# ============ DATABASE CONNECTION ============
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============ HOME ROUTE ============
@app.get("/")
def home():
    return {"message": "Student Marketplace backend running with DB"}

# ============ ADD ITEM ============
@app.post("/add-item")
def add_item(
    name: str,
    price: int,
    description: str,
    owner: str,
    college: str,
    contact: str,
    category: str,
    db: Session = Depends(get_db)
):
    new_item = models.Item(
        name=name,
        price=price,
        description=description,
        owner=owner,
        college=college,
        contact=contact,
        category=category
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {"message": "Item added successfully"}

# ============ GET ALL ITEMS ============
@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

# ============ DELETE ITEM ============
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not item:
        return {"error": "Item not found"}

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
