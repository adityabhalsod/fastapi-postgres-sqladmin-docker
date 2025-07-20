from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str

class Item(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True  # Use Pydantic v2 syntax
