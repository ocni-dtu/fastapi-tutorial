from fastapi import APIRouter

import models
from exceptions import DatabaseItemNotFound

router = APIRouter(prefix="/buildings")


@router.get("/", response_model_by_alias=False)
def get_buildings() -> list[models.Building]:
    """Get all buildings"""

    buildings = models.Building.find_all().to_list()
    return buildings


@router.post("/", status_code=201, response_model_by_alias=False)
def create_building(building: models.Building) -> models.Building:
    """Create a new building"""

    building.create()

    return building


@router.put("/{uid}", response_model_by_alias=False)
def update_building(uid: str, changes: models.UpdateBuilding) -> models.Building:
    """Update a Building with new values"""

    building = models.Building.get(uid).run()
    if not building:
        raise DatabaseItemNotFound(f"Could not find Building with id: {uid}")

    for key, value in changes.dict(exclude_unset=True).items():
        setattr(building, key, value)
    building.save()

    return building


@router.delete("/{uid}")
def delete_building(uid: str) -> str:
    """Delete a Building"""

    building = models.Building.get(uid).run()
    if not building:
        raise DatabaseItemNotFound(f"Could not find Building with id: {uid}")
    building.delete()

    return uid
