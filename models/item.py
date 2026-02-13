from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str
    owner: str
    college: str
    contact: str
    category: str
