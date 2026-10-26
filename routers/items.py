from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
	name: str
	price: float
	is_offer: Optional[bool] = None


@router.get("/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
	return {"item_id": item_id, "q": q}
	
@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
	return {"item_name": item.name, "item_id": item_id}