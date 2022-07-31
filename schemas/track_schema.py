from typing import Optional
from pydantic import BaseModel


class BaseTrack(BaseModel):
    TrackId: int
    Name: str
    Composer: Optional[str] = None
    Milliseconds: int
    Bytes: int
    UnitPrice: float
    class Config:
        orm_mode = True


class AllDataInTrack(BaseModel):
    AlbumTitle: str
    TrackName: str
    TrackPrice: float
    TrackId: int
    Composer: Optional[str] = None
    Milliseconds: int
    Bytes: int
    ArtistName: str
    GenreName: str
    MediaTypeName: str
    
    class Config:
        orm_mode = True

