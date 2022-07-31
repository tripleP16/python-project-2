from config_db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.track_model import Track
class Genre(Base):
    __tablename__ = "genres"
    GenreId = Column(Integer, primary_key=True, )
    Name = Column(String, nullable=False,   )
    Tracks = relationship("Track")