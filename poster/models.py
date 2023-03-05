from core.config import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    tittle = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')