from sqlalchemy.orm import Session
from mod_user import User
from .read import get_user_by_name_and_age

def create_user(name: str, age: int, db: Session) -> User | None:
    user: User | None = get_user_by_name_and_age(name, age, db)
    if user: print("User alredy exists.") ; return
    
    db_user = User(name= name, age= age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user