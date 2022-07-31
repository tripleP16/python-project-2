from config_db import SessionLocal
from repositories.artist_repository import ArtistRepository
from repositories.track_repository import TrackRepository
from test.config_test_db import TestingSessionLocal

# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_artist_repo():
    return ArtistRepository()

def get_track_repo():
    return TrackRepository()

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()