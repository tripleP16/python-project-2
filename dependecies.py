from config_db import SessionLocal
from repositories.artist_repository import ArtistRepository

# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_artist_repo():
    return ArtistRepository()