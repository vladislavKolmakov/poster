from fastapi import APIRouter
from poster import posts

router = APIRouter()

router.include_router(posts.router, prefix='/post')