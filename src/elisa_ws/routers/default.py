from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "ELISa REST API"}


@router.get("/ping/?", name='Health Check')
async def root():
    return {"message": "pong!"}
