

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from dependecies import get_artist_repo, get_db
from repositories.artist_repository import ArtistRepository
from repositories.track_repository import TrackRepository

from schemas.track_schema import BaseTrack
from config_db import SessionLocal

router = APIRouter(
    prefix="/singer",
    tags=["Singer"],
)

@router.get("/{id}", response_model= List[BaseTrack], status_code=status.HTTP_200_OK, name="singer-songs")
async def get_singer_songs(
    id: int,
    db: SessionLocal = Depends(get_db),
    repository: ArtistRepository = Depends(get_artist_repo),
    ):
    track_list = await repository.get_all_artist_tracks(id, db)
    if not track_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return track_list