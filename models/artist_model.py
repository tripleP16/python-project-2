from sqlalchemy import Column, Integer, String
from config_db import Base
from sqlalchemy.orm import declarative_base, relationship
from models.album_model import Album

class Artist(Base):
    __tablename__ = "artists"
    ArtistId = Column(Integer, primary_key=True, )
    Name = Column(String, nullable=False,   )
    albums = relationship("Album")

