from fastapi import APIRouter

from routes import building

router = APIRouter()
router.include_router(building.router, tags=["building"])
