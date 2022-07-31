from typing import List
from config_db import SessionLocal
from models.track_model import Track
from schemas.track_schema import BaseTrack


class TrackRepository:
    async  def get_all_tracks_by_album_id(self, id: int, db: SessionLocal)->List[BaseTrack]:
        track_list: List[BaseTrack] = db.query(Track).filter(Track.AlbumId == id).all()
        return track_list
        