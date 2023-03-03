from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, Boolean
from datetime import datetime

metadata = MetaData()

note = Table(
    'post',
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
    Column('hashed_password', String, nullable=True),
    Column('age', Integer, nullable=True),
    Column('gender', String, nullable=True),
    Column('registred_at', TIMESTAMP, default=datetime.utcnow),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)