from fastapi import FastAPI
from app.core.cors import add_cors
from app.api.routes import upload, search, health

app = FastAPI(title="Lost & Found AI")

add_cors(app)

app.include_router(health.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(search.router, prefix="/api")
