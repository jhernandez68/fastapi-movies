from src.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Movie(Base):
    """sql model for movie

    Args:
        Base (_type_): _description_
    """
    __tablename__ = "movies"
    
    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    title : Mapped[str] = mapped_column(nullable=False)
    release_date : Mapped[str] = mapped_column(nullable=False)
    genre_id : Mapped[int] = mapped_column(ForeignKey("genres.id"), nullable=False)

    genre : Mapped["Genre"] = relationship(back_populates="movies") # type: belongsTo