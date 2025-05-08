from sqlalchemy.orm import Session

from src.modules.movies.database.models import movie_sql_model
from src.modules.movies.schemas import movie
sql_model= movie_sql_model.Movie
create_model_schema = movie.MovieCreate

def get_one_movie(db: Session, movie_id: int):
    return db.query(sql_model).filter(sql_model.id == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_model).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: create_model_schema):
    db_movie = sql_model(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie: create_model_schema):
    db_movie = db.query(sql_model).filter(sql_model.id == movie_id).first()
    if db_movie is None:
        return None
    updated_data = movie.model_dump()
    for key, value in updated_data.items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(sql_model).filter(sql_model.id == movie_id).first()
    if db_movie is None:
        return None
    db.delete(db_movie)
    db.commit()
    return db_movie