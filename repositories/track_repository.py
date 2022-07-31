from typing import List
from config_db import SessionLocal
from models.album_model import Album
from models.artist_model import Artist
from models.genre_model import Genre
from models.media_type_model import MediaType
from models.track_model import Track
from schemas.track_schema import AllDataInTrack, BaseTrack


class TrackRepository:
    async def get_all_tracks_by_album_id(self, id: int, db: SessionLocal)->List[BaseTrack]:
        track_list: List[BaseTrack] = db.query(Track).filter(Track.AlbumId == id).all()
        return track_list
    
    async def get_track_by_id(self, id: int, db: SessionLocal)->AllDataInTrack:
        track: AllDataInTrack = db.query(Track).select_from(Track).with_entities(
            Album.Title.label('AlbumTitle'), 
            Track.Name.label('TrackName'), 
            Track.UnitPrice.label('TrackPrice'),
            Track.TrackId.label('TrackId'),
            Track.Composer.label('Composer'),
            Track.Milliseconds.label('Milliseconds'),
            Track.Bytes.label('Bytes'),
            Artist.Name.label('ArtistName'),
            Genre.Name.label('GenreName'),
            MediaType.Name.label('MediaTypeName')

            ).filter(Track.TrackId == id).join(Album).join(Artist).join(Genre).join(MediaType).first()
        return track