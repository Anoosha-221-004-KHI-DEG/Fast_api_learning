from fastapi import FastAPI

app = FastAPI() #created Fastapi instance

@app.get("/")
def index():
    return {"data": {"name":"abc"}}



@app.get("/about")
def about():
    return {"data": {"about page"}}