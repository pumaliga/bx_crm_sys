from sqlalchemy import Column, Integer, String
from . import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    password = Column(String(100))
    first_name = Column(String(120))
    last_name = Column(String(120))
    num_phone = Column(String(9))
    wallet = Column(Integer, default=0)


