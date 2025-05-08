from fastapi import APIRouter, Depends
from src.types import APIGetResponseType, APIResponseType, APIGetOneResponseType
from src.modules.movies.schemas.movie import MovieCreate,Movie
from src.database import SessionLocal
from src.modules.movies.database.crud import movies as movies_crud
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/movies",
    tags=["movies -> movies"]
)

def convert_models_to_schemas(output,schema):
    return [schema.model_validate(i) for i in output]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=APIGetResponseType[Movie])
async def get_movies(db:Session=Depends(get_db)) -> APIGetResponseType[Movie]:
    """Get many of movie

    Returns:
        APIGetResponseType[Movie]: Response for the api
    """
    
    result= movies_crud.get_movies(db)    
    data = convert_models_to_schemas(result,Movie) 
    response = APIGetResponseType[Movie](ok="movies retrieved succesfully",items=data)
    return response

@router.get("/{movie_id}", response_model=APIGetOneResponseType[Movie])
async def get_one_movie(movie_id:int, db:Session=Depends(get_db)) -> APIGetOneResponseType[Movie]:
    """Get One result for movie

    Args:
       movie_id (int): id for the movie to query
    
    Returns:
        APIGetOneResponseType[Movie]: Response for the API.
    """
    
    data = Movie.model_validate(movies_crud.get_one_movie(db,movie_id))
    response = APIGetOneResponseType[Movie](ok=" retrieved succesfully",item=data)
    return response

@router.post("/", response_model=APIResponseType[str])
async def post_movies(item:MovieCreate, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Create one of movie

    Args:
        item (Movie): movie to be created

    Returns:
        APIResponseType[Movie]: Response for the api
    """
    movies_crud.create_movie(db,item)
    response= APIResponseType[str](ok=True,message=" created successfully")
    return response

@router.put("/{movie_id}", response_model=APIResponseType[str])
async def put_movies(movie_id:int, item:MovieCreate, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Update one of movie

    Args:
        movie_id (int): id for the movie to query
        item (Movie): the body of the movie to be updated

    Returns:
        APIResponseType[str]: Response for the api
    """
    movies_crud.update_movie(db, movie_id, item)
    response = APIResponseType[str](ok=True, message=" updated successfully")
    return response

@router.delete("/{movie_id}", response_model=APIResponseType[str])
async def delete_movies(movie_id:int, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Delete one of movie

    Args:
       movie_id (int): id for the movie to query

    Returns:
        APIResponseType[str]: Response for the api
    """
    movies_crud.delete_movie(db, movie_id)
    response = APIResponseType[str](ok=True, message=" deleted successfully")
    return response