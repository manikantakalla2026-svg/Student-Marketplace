from fastapi import APIRouter
from models.item import Item

router = APIRouter()

items_db = []

@router.post("/add-item")
def add_item(item: Item):
    items_db.append(item)
    return {"message": "Item added", "data": item}

@router.get("/items")
def get_items():
    return items_db

@router.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            items_db.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}
