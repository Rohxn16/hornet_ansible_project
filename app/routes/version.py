from fastapi import APIRouter
from core.config import settings

router = APIRouter()

@router.get("/version")
def version():
    return {"version": settings.app_version}
