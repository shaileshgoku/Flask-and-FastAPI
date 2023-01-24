from fastapi import FastAPI

app = FastAPI()   #path or route

@app.get("/")
def fruit():
    return {"fruit":"orange"}