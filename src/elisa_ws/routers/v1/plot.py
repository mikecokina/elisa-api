from fastapi import APIRouter

router = APIRouter()


@router.get("/equipotential/", tags=["equipotential"])
async def equipotential():
    return {"plot": "data"}
