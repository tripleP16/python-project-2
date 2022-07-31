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

