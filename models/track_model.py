from sqlalchemy import Column, ForeignKey, Integer, String
from config_db import Base
class Track(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True, )
    Name = Column(String, nullable=False,   )
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"), nullable=False, )
    MediaTypeId = Column(Integer, ForeignKey("media_types.MediaTypeId"), nullable=False, )
    GenreId = Column(Integer, ForeignKey("genres.GenreId"), nullable=False, )
    Composer = Column(String, nullable=True,   )
    Milliseconds = Column(Integer, nullable=False,   )
    Bytes = Column(Integer, nullable=False,   )
    UnitPrice = Column(String, nullable=False,   )
