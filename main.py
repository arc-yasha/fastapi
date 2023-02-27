from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get():
    return {"Hello": "World"}


@app.post("/")
def post():
    return {"message": "Hello from post route"}
