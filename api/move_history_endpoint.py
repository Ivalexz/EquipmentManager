from fastapi import APIRouter
from services.move_history_service import MoveHistoryService

service = MoveHistoryService(None)
router=APIRouter()

@router.get("/move_history")
def get_all():
    return service.get_all_move_history()

@router.get("/move_history/equipment/{equipment_id}")
def get_by_equipment_id(equipment_id: int):
    return service.get_move_history_by_equipment_id(equipment_id)

@router.post("/move_history/move")
def move_equipment(equipment_id: int, new_location: str):
    res = service.move_equipment(equipment_id, new_location)
    if res is None:
        return {"error": "Equipment not found"}
    return res
