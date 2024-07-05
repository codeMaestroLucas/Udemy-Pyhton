from sqlalchemy.orm import Session

def select(table_name: str, *values, db: Session) -> str|None:
    
    ...