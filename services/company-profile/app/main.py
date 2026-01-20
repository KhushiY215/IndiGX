from fastapi import FastAPI
from .api.profile_routes import router

app = FastAPI(title="Company Profile Service")

app.include_router(router)
