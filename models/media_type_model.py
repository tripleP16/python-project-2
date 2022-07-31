from config_db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.track_model import Track

class MediaType(Base):
    __tablename__ = "media_types"
    MediaTypeId = Column(Integer, primary_key=True, )
    Name = Column(String, nullable=False,   )
    Tracks = relationship("Track")