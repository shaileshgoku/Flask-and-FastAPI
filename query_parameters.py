from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"hello"}

# @app.get("/fruits")  # ("/fruits") -> path parameters
# def fruits(name : str, weight : str):  # (name: str, weight: str) are query parameters which is not part of path parameters
#     return {"fruit_name": name, "fruit_weight":weight}

# for query parameters we have to write fruits/?name=mango&weight=20kg in the path of https link

# @app.get("/fruits")  # ("/fruits") -> path parameters
# def fruits(count : int, weight : int):  # (name: str, weight: str) are query parameters which is not part of path parameters
#     return {"fruit_count": count, "fruit_weight":weight}

@app.get("/fruits")  # ("/fruits") -> path parameters
def fruits(count : int=12, weight : int=2):  # (name: str, weight: str) are query parameters which is not part of path parameters
    return {"fruit_count": count, "fruit_weight":weight}

