from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PutItem(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class CreateItem(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
async def read_root():
  return { "hello" : "world" }

@app.get("/items/{item_id}")
async def read_item(item_id:int, q:Optional[str]=None):
  return{ "item_id" : item_id, "q" : q }


@app.put("/items/{item_id}")
def update_item(item_id:int, item:PutItem):
  return { "item_name" : item.name, "item_id" : item_id }

@app.post("/items/")
async def create_item(item: CreateItem):
	return item