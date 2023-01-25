# from fastapi import FastAPI 

# app = FastAPI()

# @app.get("/")
# def hello():
#     return "hello"

# @app.get("/{item}")
# def show_item(item):
#     return {"items":item}

from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def hello():
    return "hello"

@app.get("/{item}")
def show_item(item : int):
    return {"items":item}

from fastapi import FastAPI 

# app = FastAPI()

# @app.get("/")
# def hello():
#     return "hello"

# @app.get("/{item}")
# def show_item(item : str):
#     return {"items":item}
