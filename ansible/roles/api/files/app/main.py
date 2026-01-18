from fastapi import FastAPI
from routes import health, version, ingest

app = FastAPI(title="Data Platform API")

app.include_router(health.router)
app.include_router(version.router)
app.include_router(ingest.router)
