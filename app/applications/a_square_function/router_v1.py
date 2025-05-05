from fastapi import APIRouter
from project.project_1.v1.endpoints import (
    hello,
)

prefix = "/v1"
api_router = APIRouter()


api_router.include_router(
    hello.api_router, prefix=prefix, tags=["project_1"]
)