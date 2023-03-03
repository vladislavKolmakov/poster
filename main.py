from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

app = FastAPI(
    title='Poster'
)

#################################

fake_users = [
    {'id': 0, 'name': 'Anton', 'surname': 'Belyaev', 'hashed_password': '123', 'age': 23, 'nickname': 'ANTONIDAS', 'gender': 'male', 'registred_at': '2020-01-01T00:00:00', 'is_active': True, 'is_superuser': False, 'is_verified': True},
    {'id': 1, 'name': 'Vladislav', 'surname': 'Kolmakov', 'hashed_password': '123', 'age': 24, 'nickname': 'imfoslash', 'gender': 'male', 'registred_at': '2020-01-01T00:00:00', 'is_active': True, 'is_superuser': True, 'is_verified': True},
    {'id': 2, 'name': 'Sonya', 'surname': 'Chukanova', 'hashed_password': '123', 'age': 27, 'nickname': 'kotik', 'gender': 'female', 'registred_at': '2020-01-01T00:00:00', 'is_active': True, 'is_superuser': False, 'is_verified': True},
]

fake_posts = [
    {'id': 0, 'uid': 1, 'content': 'встал, покушал, в целом не плохо'},
    {'id': 1, 'uid': 0, 'content': 'я верховный архимаг АНТОНИДОС!!!'},
    {'id': 2, 'uid': 2, 'content': 'мяу мяу мяу'},
]

#################################


class User(BaseModel):
    id: int
    name: str
    surname: str
    hashed_password: str
    password: str
    age: int = Field(ge=0)
    gender: str
    registred_at: datetime
    registred_at: bool
    is_active: bool
    is_verified: bool

class Post(BaseModel):
    id: int
    uid: int
    content: str

#################################


# TODO fing all posts by user.name/user.surname/user.nickname/date
@app.get('/get_posts/{posts_id}', response_model=List[Post])
def get_posts(posts_id: int):
    return [posts for posts in fake_posts  if posts.get('id') == posts_id]

# TODO find user by user.name/user.surname/user.nickname
@app.get('/get_user/{user_id}')
def get_user(user_id: int):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    return current_user


@app.post('/create_post')
def add_post(post: List[Post]):
    fake_posts.extend(post)
    return {'status': 200, 'data': fake_posts}