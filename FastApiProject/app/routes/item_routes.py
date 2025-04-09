from fastapi import APIRouter, status
from app.schemas.item_schema import Item, ItemUpdate
from app.services.item_service import create_item, get_item, get_all_items, update_item, delete_item

router = APIRouter()

@router.post("/items/", status_code=status.HTTP_201_CREATED)
def create(item: Item):
    return create_item(item)

@router.get("/items/{item_id}")
def read(item_id: str):
    return get_item(item_id)

@router.get("/items/")
def read_all():
    return get_all_items()

@router.put("/items/{item_id}")
def update(item_id: str, item: ItemUpdate):
    return update_item(item_id, item)

@router.delete("/items/{item_id}")
def delete(item_id: str):
    return delete_item(item_id)
