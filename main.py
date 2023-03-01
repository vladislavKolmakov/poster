from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(
    title='Poster'
)

#################################

fake_users = [
    {'id': 0, 'name': 'Anton', 'surname': 'Belyaev', 'age': 23, 'nickname': 'ANTONIDAS', 'sex': 'male'},
    {'id': 1, 'name': 'Vladislav', 'surname': 'Kolmakov', 'age': 24, 'nickname': 'imfoslash', 'sex': 'male'},
    {'id': 2, 'name': 'Sonya', 'surname': 'Chukanova', 'age': 27, 'nickname': 'kotik', 'sex': 'female'},
]

fake_posts = [
    {'id': 0, 'uid': 1, 'content': 'встал, покушал, в целом не плохо'},
    {'id': 1, 'uid': 0, 'content': 'я верховный архимаг АНТОНИДОС!!!'},
    {'id': 2, 'uid': 2, 'content': 'мяу мяу мяу'},
]

#################################


# TODO fing all posts by user.name/user.surname/user.nickname/date
@app.get('/get_post/{post_id}')
def hello(post_id: int):
    return [post for post in fake_posts  if post.get('id') == post_id]

# TODO find user by user.name/user.surname/user.nickname
@app.get('/get_user/{user_id}')
def get_user(user_id: int):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    return {"status": 200, "data": current_user}