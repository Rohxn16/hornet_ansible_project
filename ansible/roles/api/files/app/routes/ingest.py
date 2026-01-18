from fastapi import APIRouter
from services.ingest_service import ingest_user

router = APIRouter()

@router.post("/ingest")
def ingest(payload: dict):
    ingest_user(payload)
    return {"status": "stored"}
