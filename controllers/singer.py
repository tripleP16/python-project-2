

from fastapi import APIRouter, status


router = APIRouter(
    prefix="/singer",
    tags=["Singer"],
)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_singer_songs(id: int):
    return {"id": id}