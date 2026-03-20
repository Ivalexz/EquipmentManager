from pydantic import BaseModel
from enums import EquipmentType, EquipmentStatus


class Equipment(BaseModel):
    id: int
    name: str
    type: EquipmentType
    model: str
    manufacturer: str
    year: int
    price: float
    location: str
    status: EquipmentStatus