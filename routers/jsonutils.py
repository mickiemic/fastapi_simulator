from fastapi import APIRouter
import json
from typing import List, Dict, Any
from pydantic import BaseModel

router = APIRouter()

class JsonPayload(BaseModel):
    data: Dict[str, Any]

@router.post("/intersect")
async def json_intersect(items: List[Dict[str, Any]]):
    #pLen = len(items)
    #strPlayload = json.dumps(items, sort_keys=True)
    # print(f'payload: {strPlayload}')
    
    # Finds the common keys
    common_keys = set.intersection(*map(set, items))

    return {"common_keys": common_keys}

@router.post("/deintersect")
async def json_deintersect(items: List[Dict[str, Any]]):
    # Finds the common keys
    common_keys = set.intersection(*map(set, items))

    result = []
    for item in items:
        for ckey in common_keys:
            item.pop(ckey, None)
            
        result.append(item)

    return {"strange_keys": result}
