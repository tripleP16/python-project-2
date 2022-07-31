from fastapi import APIRouter, Depends, status
from config_db import SessionLocal
from dependecies import get_db, get_track_repo
from repositories.track_repository import TrackRepository

from schemas.track_schema import AllDataInTrack, BaseTrack

router = APIRouter(
    prefix="/song",
    tags=["Song"],
)

@router.get("/{id}", response_model= AllDataInTrack,  status_code=status.HTTP_200_OK)
async def get_song_details(id: int, db: SessionLocal = Depends(get_db), repository: TrackRepository = Depends(get_track_repo)):
    track = await repository.get_track_by_id(id, db)
    return track
