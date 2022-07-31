from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine
from controllers.singer import router as singer_router
from controllers.singers import router as singers_router
from controllers.albums import router as albums_router
from controllers.songs import router as songs_router

def get_application():

    Base.metadata.create_all(bind=engine)
    app = FastAPI(title="Music API", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    prefix = "/music-store/api/v1"

    app.include_router(singer_router, prefix=prefix)
    app.include_router(singers_router, prefix=prefix)
    app.include_router(albums_router, prefix=prefix)
    app.include_router(songs_router, prefix=prefix)
    return app

app = get_application()

@app.get("/")
def home() -> dict:
    return {"mensaje": "Bienvenido a la aplicacion de musica"}