from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Fruit(BaseModel):
    name: str
    weight: Optional[int] = None
    count: Optional[int] = None


@app.get("/")
def hello():
    return "sun"

@app.post("/fruit")
def fruits(f:Fruit):
    return {"name": f.name, "count":f.count}
