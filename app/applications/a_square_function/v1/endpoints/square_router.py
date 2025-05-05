from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/hello")
def hello(name):
    return name