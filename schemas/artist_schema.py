from pydantic import BaseModel


class Artist(BaseModel):
    ArtistId: int
    Name: str

class ArtistInBd(BaseModel):
    Name: str
    class Config:
        orm_mode = True
