from fastapi import FastAPI

from typing import Optional


app = FastAPI()

@app.get("/")
def hello():
    return "galaxy"

@app.get("/fruit/{fruit_name}/count/{total_count}")  #multiple path parameter
def fruits(total_count: int, fruit_name: str, total_weight: Optional[int] = 2):  #multiple query parameter
    return {"fruit name": fruit_name, "total count": total_count}
