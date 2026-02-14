from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models.item as models
from database import engine, SessionLocal, Base

app = FastAPI()

# create database tables
Base.metadata.create_all(bind=engine)

# dependency to get DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# home route
@app.get("/")
def home():
    return {"message": "Student Marketplace backend running with DB"}

# add item
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

    return {"message": "Item added to database"}

# get items
@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

# delete item
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    
    if not item:
        return {"error": "Item not found"}

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}
