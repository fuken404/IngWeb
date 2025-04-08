from bson import ObjectId
from fastapi import HTTPException
from app.db.database import items_collection
from app.schemas.item_schema import Item, ItemUpdate

def serialize_item(item) -> dict:
    item["id"] = str(item["_id"])
    del item["_id"]
    return item

def create_item(item: Item):
    result = items_collection.insert_one(item.dict())
    new_item = items_collection.find_one({"_id": result.inserted_id})
    return serialize_item(new_item)

def get_item(item_id: str):
    item = items_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_item(item)
    raise HTTPException(status_code=404, detail="Item not found")

def get_all_items():
    return [serialize_item(item) for item in items_collection.find()]

def update_item(item_id: str, item_data: ItemUpdate):
    result = items_collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {k: v for k, v in item_data.dict().items() if v is not None}}
    )
    if result.modified_count:
        return get_item(item_id)
    raise HTTPException(status_code=404, detail="Item not found")

def delete_item(item_id: str):
    result = items_collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
