from sqlalchemy.orm import Session

from src.modules.auth.database.models import auth_user_sql_model
from src.modules.auth.schemas import auth_user
sql_model= auth_user_sql_model.AuthUser
create_model_schema = auth_user.AuthUserCreate

def get_one_auth_user(db: Session, auth_user_id: int):
    return db.query(sql_model).filter(sql_model.id == auth_user_id).first()

def get_auth_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_model).offset(skip).limit(limit).all()

def create_auth_user(db: Session, auth_user: create_model_schema):
    db_auth_user = sql_model(**auth_user.model_dump())
    db.add(db_auth_user)
    db.commit()
    db.refresh(db_auth_user)
    return db_auth_user

def update_auth_user(db: Session, auth_user_id: int, auth_user: create_model_schema):
    db_auth_user = db.query(sql_model).filter(sql_model.id == auth_user_id).first()
    if db_auth_user is None:
        return None
    updated_data = auth_user.model_dump()
    for key, value in updated_data.items():
        setattr(db_auth_user, key, value)
    db.commit()
    db.refresh(db_auth_user)
    return db_auth_user

def delete_auth_user(db: Session, auth_user_id: int):
    db_auth_user = db.query(sql_model).filter(sql_model.id == auth_user_id).first()
    if db_auth_user is None:
        return None
    db.delete(db_auth_user)
    db.commit()
    return db_auth_user