from sqlalchemy import select
from sqlalchemy.orm import Session
from mod_user import User

def get_user_by_id(_id: int, db: Session) -> User | None:
    query = select(User).where(User.id == _id)
    try:
        user = db.execute(query).scalars().first()
        return user
    
    except:
        return

def get_user_by_name_and_age(name: str, age: int, db: Session) -> User | None:
    query = select(User).where(User.name == name, User.age == age)
    try:
        user = db.execute(query).scalars().first()
        return user
    
    except:
        return

def get_users(db: Session) -> list[User] | None:
    query = select(User)
    try:
        users = db.execute(query).scalars().all()
        return users
    
    except:
        return