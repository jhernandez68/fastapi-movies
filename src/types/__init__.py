from typing import TypeVar,Generic
from pydantic import BaseModel
T = TypeVar('T', bound=BaseModel)

class APIGetResponseType(BaseModel, Generic[T]):
    """Api Get Response

    Args:
        Generic (_type_): _description_
    """
    # items: List[T]
    ok:str
    items:list[T]

class APIGetOneResponseType(BaseModel, Generic[T]):
    """Api Get Response

    Args:
        Generic (_type_): _description_
    """
    # items: List[T]
    ok:str
    item:T

class APIResponseType(BaseModel, Generic[T]):
    """Api Get Response

    Args:
        Generic (_type_): _description_
    """
    ok:str | bool
    message:T