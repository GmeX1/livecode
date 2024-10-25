from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base


engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False}, echo=True)
session_maker = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def get_session() -> Session:
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
