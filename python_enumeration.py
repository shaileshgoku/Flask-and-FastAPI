from enum import Enum

from fastapi import FastAPI

class Fruits(str, Enum): #enum is of type str
    orange = "orange"
    apple = "apple"
    grapes = "grapes"

app = FastAPI()

@app.get("/fruits/{fruit_name}")
def get_fruit(fruit_name : Fruits):
    if fruit_name == fruit_name.orange:
        return {"Fruit_name matched": fruit_name}

    if fruit_name.value == "apple":
        return {"Fruit_name matched":fruit_name}

  

