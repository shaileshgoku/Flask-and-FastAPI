from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def add():
    return 5