from sqlalchemy import delete
from sqlalchemy.orm import Session
from mod_user import User
from .read import get_user_by_id

def delete_user_by_id(_id: int, db: Session) -> None:
    user: User|None = get_user_by_id(_id, db)

    if not user: print("Couldn't find this user") ; return

    query = delete(User).where(User.id == _id)
    db.execute(query)
    db.commit()
    print("User deleted.")