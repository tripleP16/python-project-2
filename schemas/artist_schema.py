from pydantic import BaseModel


class Artist(BaseModel):
    ArtistId: int
    Name: str

class ArtistInBd(Artist):
    class Config:
        orm_mode = True
