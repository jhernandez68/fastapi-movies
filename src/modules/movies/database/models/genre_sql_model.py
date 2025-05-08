from src.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Genre(Base):
    """sql model for genre

    Args:
        Base (_type_): _description_
    """
    __tablename__ = "genres"
    
    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str] = mapped_column(unique=True, index=True, nullable=False)

    movies : Mapped[list["Movie"]] = relationship(back_populates="genre") # type: hasMany