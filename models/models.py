from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column
from datetime import datetime

metadata = MetaData()

note = Table(
    'note',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('uid', String, nullable=False),
    Column('content', String, nullable=True),
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=True),
    Column('nickname', String, nullable=True),
    Column('password', String, nullable=True),
    Column('age', Integer, nullable=True),
    Column('gender', String, nullable=True),
    Column('registred_at', TIMESTAMP, default=datetime.utcnow),
)