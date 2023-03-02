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
    {'id': 0, 'name': 'Anton', 'surname': 'Belyaev', 'password': '123', 'age': 23, 'nickname': 'ANTONIDAS', 'gender': 'male', 'registred_at': '2020-01-01T00:00:00'},
    {'id': 1, 'name': 'Vladislav', 'surname': 'Kolmakov', 'password': '123', 'age': 24, 'nickname': 'imfoslash', 'gender': 'male', 'registred_at': '2020-01-01T00:00:00'},
    {'id': 2, 'name': 'Sonya', 'surname': 'Chukanova', 'password': '123', 'age': 27, 'nickname': 'kotik', 'gender': 'female', 'registred_at': '2020-01-01T00:00:00'},
]

fake_notes = [
    {'id': 0, 'uid': 1, 'content': 'встал, покушал, в целом не плохо'},
    {'id': 1, 'uid': 0, 'content': 'я верховный архимаг АНТОНИДОС!!!'},
    {'id': 2, 'uid': 2, 'content': 'мяу мяу мяу'},
]

#################################


class User(BaseModel):
    id: int
    name: str
    surname: str
    nickname: str = Field(max_length=20)
    password: str
    age: int = Field(ge=0)
    gender: str
    registred_at: datetime

class Note(BaseModel):
    id: int
    uid: int
    content: str

#################################


# TODO fing all posts by user.name/user.surname/user.nickname/date
@app.get('/get_notes/{notes_id}', response_model=List[Note])
def get_notes(notes_id: int):
    return [notes for notes in fake_notes  if notes.get('id') == notes_id]

# TODO find user by user.name/user.surname/user.nickname
@app.get('/get_user/{user_id}')
def get_user(user_id: int):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    return current_user


@app.post('/create_note')
def add_post(note: List[Note]):
    fake_notes.extend(note)
    return {'status': 200, 'data': fake_notes}