from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"hello":"universe"}

@app.get("/next/{items}")
def root_2(items : int):
    return {"hello":items}