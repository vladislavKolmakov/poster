from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from . schemas import PostCreate

router = APIRouter()

@router.get('/')
def post_list(db: Session = Depends(get_db)):
    post = service.get_post_list(db)
    return post

@router.post('/')
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    post = service.create_post(db, item)
    return post    