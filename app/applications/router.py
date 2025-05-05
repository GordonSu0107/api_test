from fastapi import APIRouter
from app.applications.a_square_function.router_v1 import (
    api_router as api_router_p1,
)


api_router = APIRouter()
api_router.include_router(router=api_router_p1)