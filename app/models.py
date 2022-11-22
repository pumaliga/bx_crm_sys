from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from . import db


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    password = Column(String(100))
    num_phone = Column(String(10))
    wallet = Column(Integer, default=0)


