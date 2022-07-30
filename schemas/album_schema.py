from pydantic import BaseModel
class AlbumInBd(BaseModel):
    AlbumId: int
    Title: str
    class Config:
        orm_mode = True