from sqlalchemy.orm import Session
from models.album_model import Album
from models.track_model import Track
from schemas.album_schema import AlbumInBd
from schemas.artist_schema import ArtistInBd
from typing import List
from models.artist_model import Artist
from schemas.track_schema import BaseTrack

class ArtistRepository:
    async def get_all_artist(self, db: Session) -> List[ArtistInBd]:
        artist_list: List[ArtistInBd] = db.query(Artist).all()
        return artist_list
    
    async def get_album_by_artistId(self, id: int, db: Session)->List[AlbumInBd]:
        album_list: List[AlbumInBd] = db.query(Album).filter(Album.ArtistId == id).all()
        return album_list

    async def get_all_artist_tracks(self, artist_id: int, db: Session)->List[BaseTrack]:
        track_list: List[BaseTrack] = db.query(Track).join(Album).filter(Album.ArtistId == artist_id).all()
        return track_list