import logging.config
import os

from bunnet import init_bunnet
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from core.config import settings
from core.connection import create_mongo_client
from routes import router

if "test" not in settings.SERVER_NAME.lower():
    logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.SERVER_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix=settings.API_STR)


@app.on_event("startup")
def app_init():
    """
    Run functionality on startup.
    Here we initialize the database connection.
    """

    client = create_mongo_client()
    init_bunnet(database=client[settings.DATABASE_NAME], document_models=[models.Building])

    if os.environ.get("RUN_STAGE") == "DEV":
        # Here you can place seed data
        pass
