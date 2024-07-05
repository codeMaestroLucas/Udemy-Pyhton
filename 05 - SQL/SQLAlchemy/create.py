from sqlalchemy.orm import Session
from sqlalchemy import create, select, update, delete

def create(table_name: str, *values, db: Session) -> str|None:
    
    ...