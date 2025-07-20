from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, SessionLocal
from models import Base, Item as ItemModel
from schemas import Item as ItemSchema, ItemCreate
from crud import get_items, get_item as _get_item, create_item as _create_item, update_item as _update_item, delete_item as _delete_item

from sqladmin import Admin, ModelView

app = FastAPI(title="FastAPI + PostgreSQL + SQLAdmin Example")

# ---- 1. CRUD setup (unchanged) ----

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/items/", response_model=ItemSchema)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    return await _create_item(db, item)

@app.get("/items/", response_model=list[ItemSchema])
async def read_items(db: AsyncSession = Depends(get_db)):
    return await get_items(db)

@app.get("/items/{item_id}", response_model=ItemSchema)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await _get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=ItemSchema)
async def update_item(item_id: int, item: ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = await _update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await _delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"ok": True}


# ---- 2. SQLAdmin Panel ----

# Define a ModelView for your Item model
class ItemAdmin(ModelView, model=ItemModel):
    column_list = [ItemModel.id, ItemModel.name, ItemModel.description]
    name = "Item"
    name_plural = "Items"
    icon = "fa-solid fa-table"   # any FontAwesome icon

# Initialize the admin panel
admin = Admin(app, engine)
admin.add_view(ItemAdmin)

# That's it! The Admin panel is now at /admin
