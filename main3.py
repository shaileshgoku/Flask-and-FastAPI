from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_get():
    return {"1":"2"}

@app.put("/hello")
def root_put():
    return {"1":"2"}