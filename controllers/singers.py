from typing import List
from fastapi import APIRouter, Depends, status
from config_db import SessionLocal
from dependecies import get_artist_repo, get_db
from repositories.artist_repository import ArtistRepository
from schemas.album_schema import AlbumInBd

from schemas.artist_schema import ArtistInBd

router = APIRouter(
    prefix="/singers",
    tags=["Singers"],
)
@router.get("/", response_model=List[ArtistInBd], status_code=status.HTTP_200_OK)
async def get_singers(
    db: SessionLocal = Depends(get_db),
    artist_repo: ArtistRepository = Depends(get_artist_repo),
):
    artist_list =await artist_repo.get_all_artist(db)
    return artist_list


@router.get("/{id}", response_model=List[AlbumInBd], status_code=status.HTTP_200_OK)
async def get_singer_albums(
    id: int,
    db: SessionLocal = Depends(get_db),
    artist_repo: ArtistRepository = Depends(get_artist_repo),
):
    album_list =await artist_repo.get_album_by_artistId(id, db)
    return album_list
    

