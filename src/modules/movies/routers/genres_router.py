from fastapi import APIRouter, Depends
from src.types import APIGetResponseType, APIResponseType, APIGetOneResponseType
from src.modules.movies.schemas.genre import GenreCreate,Genre
from src.database import SessionLocal
from src.modules.movies.database.crud import genres as genres_crud
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/genres",
    tags=["movies -> genres"]
)

def convert_models_to_schemas(output,schema):
    return [schema.model_validate(i) for i in output]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=APIGetResponseType[Genre])
async def get_genres(db:Session=Depends(get_db)) -> APIGetResponseType[Genre]:
    """Get many of genre

    Returns:
        APIGetResponseType[Genre]: Response for the api
    """
    
    result= genres_crud.get_genres(db)    
    data = convert_models_to_schemas(result,Genre) 
    response = APIGetResponseType[Genre](ok="genres retrieved succesfully",items=data)
    return response

@router.get("/{genre_id}", response_model=APIGetOneResponseType[Genre])
async def get_one_genre(genre_id:int, db:Session=Depends(get_db)) -> APIGetOneResponseType[Genre]:
    """Get One result for genre

    Args:
       genre_id (int): id for the genre to query
    
    Returns:
        APIGetOneResponseType[Genre]: Response for the API.
    """
    
    data = Genre.model_validate(genres_crud.get_one_genre(db,genre_id))
    response = APIGetOneResponseType[Genre](ok=" retrieved succesfully",item=data)
    return response

@router.post("/", response_model=APIResponseType[str])
async def post_genres(item:GenreCreate, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Create one of genre

    Args:
        item (Genre): genre to be created

    Returns:
        APIResponseType[Genre]: Response for the api
    """
    genres_crud.create_genre(db,item)
    response= APIResponseType[str](ok=True,message=" created successfully")
    return response

@router.put("/{genre_id}", response_model=APIResponseType[str])
async def put_genres(genre_id:int, item:GenreCreate, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Update one of genre

    Args:
        genre_id (int): id for the genre to query
        item (Genre): the body of the genre to be updated

    Returns:
        APIResponseType[str]: Response for the api
    """
    genres_crud.update_genre(db, genre_id, item)
    response = APIResponseType[str](ok=True, message=" updated successfully")
    return response

@router.delete("/{genre_id}", response_model=APIResponseType[str])
async def delete_genres(genre_id:int, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Delete one of genre

    Args:
       genre_id (int): id for the genre to query

    Returns:
        APIResponseType[str]: Response for the api
    """
    genres_crud.delete_genre(db, genre_id)
    response = APIResponseType[str](ok=True, message=" deleted successfully")
    return response