from fastapi import FastAPI
from .api.partnership_routes import router

app = FastAPI(title="Partnership & Ecosystem Service")

app.include_router(router)
