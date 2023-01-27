from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def hello():
    return {"File":"Fileupload"}

@app.post("/file")
def create_f(file: bytes = File(...)): #this will work for short files #for file datatype is bytes, this is compulsory
    return {"file size": len(file)}

@app.post("/uploaded_f") #this will work for bigger files also
def uploaded_f(file: UploadFile):
    return {"filename":file.filename}