from settings import Base, engine, get_db
from CRUD.create import create_user
from CRUD.read import get_users
from CRUD.update import update_user
from CRUD.delete import delete_user_by_id

def main() -> None:
    """Function used to run the main code."""
    Base.metadata.create_all(bind= engine)
    db = next(get_db())
    
    user1 = create_user(name= "Lucas", age= 32, db= db)
    user2 = create_user(name= "Anna", age= 25, db= db)

    print(f"Created Users: {user1}, {user2}")

    print(get_users(db))

    print(update_user(1, "Lucas", "23", db))

    delete_user_by_id(2, db)
    
    print(get_users(db))


if __name__ == '__main__':
    main()