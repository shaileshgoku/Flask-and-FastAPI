## string validation

from fastapi import FastAPI, Query
from typing import Optional


app = FastAPI()

@app.get("/")
def hello():
    return "mars"

@app.get("/fruit/")
def fruits(fruit_name: str = Query(..., min_length=2, max_length=5)):
    return {"This is query parameter additional options": fruit_name}

