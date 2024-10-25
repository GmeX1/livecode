from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from database.models import User, Cart
from schemas.user_schemas import UserSchema

user_router = APIRouter()


@user_router.get('/get_users')
def get_users(session: Session = Depends(get_session)):
    result = session.execute(select(User))
    return {'result': result.all()}


@user_router.get('/get_user/{user_id}')
def get_user(user_id: int, session: Session = Depends(get_session)):
    result = session.execute(select(User).where(User.id == user_id))
    return {'result': result.all()}


@user_router.post('/add_user')
def add_user(user: UserSchema, session: Session = Depends(get_session)):
    new_cart = Cart()
    session.add(new_cart)
    new_user = User(name=user.name, cart_id=new_cart.id)
    session.add(new_user)
    session.commit()
    return {'result': new_user}


@user_router.patch('/edit_user/{user_id}')
def edit_user(user_id: int, new_data):
    pass


@user_router.delete('/delete_user/{user_id}')
def delete_user(user_id: int):
    pass
