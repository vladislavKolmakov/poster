from sqlalchemy.orm import Session
from core.base import Post
from .schemas import PostCreate
# ? why impoty bellow rise annot import name 'User' from partially initialized module 'user.models'
# from .models import Post




def get_post_list(db: Session):
    return db.query(Post).all()


def create_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post