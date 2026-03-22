from pydantic import BaseModel

class EquipmentMovesHistory(BaseModel):
    id: int
    equipment_id: int
    from_location: str
    to_location: str
    move_date: str