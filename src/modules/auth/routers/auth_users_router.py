from fastapi import APIRouter, Depends
from src.types import APIGetResponseType, APIResponseType, APIGetOneResponseType
from src.modules.auth.schemas.auth_user import AuthUserCreate,AuthUser
from src.database import SessionLocal
from src.modules.auth.database.crud import auth_users as auth_users_crud
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth_users",
    tags=["auth -> auth_users"]
)

def convert_models_to_schemas(output,schema):
    return [schema.model_validate(i) for i in output]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=APIGetResponseType[AuthUser])
async def get_auth_users(db:Session=Depends(get_db)) -> APIGetResponseType[AuthUser]:
    """Get many of auth_user

    Returns:
        APIGetResponseType[AuthUser]: Response for the api
    """
    
    result= auth_users_crud.get_auth_users(db)    
    data = convert_models_to_schemas(result,AuthUser) 
    response = APIGetResponseType[AuthUser](ok="auth_users retrieved succesfully",items=data)
    return response

@router.get("/{auth_user_id}", response_model=APIGetOneResponseType[AuthUser])
async def get_one_auth_user(auth_user_id:int, db:Session=Depends(get_db)) -> APIGetOneResponseType[AuthUser]:
    """Get One result for auth_user

    Args:
       auth_user_id (int): id for the auth_user to query
    
    Returns:
        APIGetOneResponseType[AuthUser]: Response for the API.
    """
    
    data = AuthUser.model_validate(auth_users_crud.get_one_auth_user(db,auth_user_id))
    response = APIGetOneResponseType[AuthUser](ok=" retrieved succesfully",item=data)
    return response

@router.post("/", response_model=APIResponseType[str])
async def post_auth_users(item:AuthUserCreate, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Create one of auth_user

    Args:
        item (AuthUser): auth_user to be created

    Returns:
        APIResponseType[AuthUser]: Response for the api
    """
    auth_users_crud.create_auth_user(db,item)
    response= APIResponseType[str](ok=True,message=" created successfully")
    return response

@router.put("/{auth_user_id}", response_model=APIResponseType[str])
async def put_auth_users(auth_user_id:int, item:AuthUserCreate, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Update one of auth_user

    Args:
        auth_user_id (int): id for the auth_user to query
        item (AuthUser): the body of the auth_user to be updated

    Returns:
        APIResponseType[str]: Response for the api
    """
    auth_users_crud.update_auth_user(db, auth_user_id, item)
    response = APIResponseType[str](ok=True, message=" updated successfully")
    return response

@router.delete("/{auth_user_id}", response_model=APIResponseType[str])
async def delete_auth_users(auth_user_id:int, db:Session=Depends(get_db)) -> APIResponseType[str]:
    """Delete one of auth_user

    Args:
       auth_user_id (int): id for the auth_user to query

    Returns:
        APIResponseType[str]: Response for the api
    """
    auth_users_crud.delete_auth_user(db, auth_user_id)
    response = APIResponseType[str](ok=True, message=" deleted successfully")
    return response