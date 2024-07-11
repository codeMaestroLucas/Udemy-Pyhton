from sqlalchemy import update
from sqlalchemy.orm import Session
from mod_user import User
from .read import get_user_by_id

def update_user(_id: int, new_name: str, new_age: int, db: Session) -> User | None:
    user: User | None = get_user_by_id(_id, db)

    if not user: print("Couldn't find this user.") ; return

    query = update(User).where(User.id == _id).values(
        name= new_name,
        age= new_age,
    )
    db.execute(query)
    db.commit()
        
    return get_user_by_id(_id, db)