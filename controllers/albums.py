from typing import List
from fastapi import APIRouter, Depends, status
from config_db import SessionLocal
from dependecies import get_artist_repo, get_db, get_track_repo
from repositories.artist_repository import ArtistRepository
from repositories.track_repository import TrackRepository

from schemas.track_schema import BaseTrack

router=APIRouter(
    prefix="/albums",
    tags=["Albums"]
)
@router.get("/{id}", response_model= List[BaseTrack], status_code=status.HTTP_200_OK)
async def get_album_songs(id: int, db: SessionLocal = Depends(get_db), repository: TrackRepository = Depends(get_track_repo)):
    track_list = await repository.get_all_tracks_by_album_id(id, db)
    return track_list

