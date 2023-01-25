from fastapi import FastAPI

app = FastAPI() #created Fastapi instance

@app.get("/")
def index():
    return {"data": "blog list"}



@app.get("/blog/{id}")
def about(id):
    return {"data": id}