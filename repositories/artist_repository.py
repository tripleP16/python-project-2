from sqlalchemy.orm import Session
from models.album_model import Album
from schemas.album_schema import AlbumInBd
from schemas.artist_schema import ArtistInBd
from typing import List
from models.artist_model import Artist

class ArtistRepository:
    async def get_all_artist(self, db: Session) -> List[ArtistInBd]:
        artist_list: List[ArtistInBd] = db.query(Artist).all()
        return artist_list
    
    async def get_album_by_artistId(self, id: int, db: Session)->List[AlbumInBd]:
        album_list: List[AlbumInBd] = db.query(Album).filter(Album.ArtistId == id).all()
        return album_list