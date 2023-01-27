from fastapi import FastAPI, Form


app = FastAPI()

@app.get("/")
def hello():
    return "galaxy"

@app.post("/signup")
def signup(user_name: str = Form(...), phone_no: int = Form(...)):
    return {"user name": user_name}
