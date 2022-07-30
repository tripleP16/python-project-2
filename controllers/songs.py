from fastapi import APIRouter, status

router = APIRouter(
    prefix="/song",
    tags=["Song"],
)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_song_details(id: int):
    return {"id": id}
