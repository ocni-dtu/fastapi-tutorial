from uuid import UUID, uuid4

from bunnet import Document
from pydantic import BaseModel, Field, root_validator


class UpdateBuilding(BaseModel):
    name: str | None
    address: str | None
    owner: str | None


class Building(Document, UpdateBuilding):
    """Building"""

    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str
    address: str
    owner: str

    class Settings:
        name = "buildings"
