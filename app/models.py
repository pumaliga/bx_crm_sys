from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from . import db


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    password = Column(String(100))
    num_phone = Column(String(10))
    wallet = Column(Integer, default=0)


class Categories(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    product = relationship('Products', backref='categories')


class Products(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    vendor_code = Column(String(30))
    desc = Column(String(120))
    price = Column(Numeric(5, 2))
    count = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'))
    images = relationship('Images', backref='products')


class Images(db.Model):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    product_id = Column(Integer, ForeignKey('products.id'))
