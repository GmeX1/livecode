from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))


cart_products = Table(
    'cart_products',
    Base.metadata,
    Column('cart_id', Integer, ForeignKey('carts.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)


class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    restricted: Mapped[bool] = mapped_column(default=False)
    price: Mapped[float]
    carts = relationship('Cart', secondary=cart_products, back_populates='products')


class Cart(Base):
    __tablename__ = 'carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int] = mapped_column(default=0)
    products: Mapped[List['Product']] = relationship('Product', secondary=cart_products, back_populates='carts')
