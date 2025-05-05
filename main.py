from fastapi import FastAPI, APIRouter
from app.applications.router import api_router


app=FastAPI()
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Hello from root!"}