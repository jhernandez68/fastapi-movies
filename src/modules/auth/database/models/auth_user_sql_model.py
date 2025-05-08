from src.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class AuthUser(Base):
    """sql model for auth_user

    Args:
        Base (_type_): _description_
    """
    __tablename__ = "auth_users"
    
    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    username : Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password : Mapped[str] = mapped_column(nullable=False)