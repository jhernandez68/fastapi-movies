from pydantic import BaseModel        

class AuthUserBase(BaseModel):
    username: str
    hashed_password: str

class AuthUserCreate(AuthUserBase):
    pass

class AuthUser(AuthUserBase):
    id: int
    class Config:
        from_attributes = True