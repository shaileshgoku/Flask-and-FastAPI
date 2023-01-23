from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def typeHints(name: str, height: int):
    print("your name is "+ name +" and your height is "+ height)