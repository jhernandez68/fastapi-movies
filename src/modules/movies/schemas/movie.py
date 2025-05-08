from pydantic import BaseModel        

class MovieBase(BaseModel):
    title: str
    release_date: str
    genre_id: int

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    class Config:
        from_attributes = True