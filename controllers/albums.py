from fastapi import APIRouter, status

router=APIRouter(
    prefix="/albums",
    tags=["Albums"]
)
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_album_songs(id: int):
    return {"id": id}

