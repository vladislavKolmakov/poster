from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI(
    title='Poster'
)

#################################

fake_users = [
    {'id': 0, 'name': 'Anton', 'surname': 'Belyaev', 'age': 23, 'nickname': 'ANTONIDAS', 'gender': 'male'},
    {'id': 1, 'name': 'Vladislav', 'surname': 'Kolmakov', 'age': 24, 'nickname': 'imfoslash', 'gender': 'male'},
    {'id': 2, 'name': 'Sonya', 'surname': 'Chukanova', 'age': 27, 'nickname': 'kotik', 'gender': 'female'},
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
    age: int = Field(ge=0)
    gender: str

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