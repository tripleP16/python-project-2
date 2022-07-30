from sqlalchemy import Column, ForeignKey, Integer, String
from config_db import Base


class Album(Base):
    __tablename__ = "albums"
    AlbumId = Column(Integer, primary_key=True, )
    Title = Column(String, nullable=False,   )
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"), nullable=False, )