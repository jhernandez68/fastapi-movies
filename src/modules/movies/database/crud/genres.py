from sqlalchemy.orm import Session

from src.modules.movies.database.models import genre_sql_model
from src.modules.movies.schemas import genre
sql_model= genre_sql_model.Genre
create_model_schema = genre.GenreCreate

def get_one_genre(db: Session, genre_id: int):
    return db.query(sql_model).filter(sql_model.id == genre_id).first()

def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_model).offset(skip).limit(limit).all()

def create_genre(db: Session, genre: create_model_schema):
    db_genre = sql_model(**genre.model_dump())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def update_genre(db: Session, genre_id: int, genre: create_model_schema):
    db_genre = db.query(sql_model).filter(sql_model.id == genre_id).first()
    if db_genre is None:
        return None
    updated_data = genre.model_dump()
    for key, value in updated_data.items():
        setattr(db_genre, key, value)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def delete_genre(db: Session, genre_id: int):
    db_genre = db.query(sql_model).filter(sql_model.id == genre_id).first()
    if db_genre is None:
        return None
    db.delete(db_genre)
    db.commit()
    return db_genre