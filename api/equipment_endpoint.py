from services.equipment_service import EquipmentService
from models import Equipment
from models.enums import EquipmentStatus
from fastapi import FastAPI

service=EquipmentService()

app=FastAPI()

@app.get("/")
def get_all():
    return service.get_all_equipment()

@app.get("/equipment/{id}")
def get_by_id(id:int):
    return service.get_equipment_by_id(id)

@app.post("/equipment/add")
def add_equipment(equipment: Equipment):
    return service.add_equipment(equipment)

@app.patch("/equipment/{id}/status")
def update_status(id: int, new_status: EquipmentStatus):
    return service.update_status(id, new_status)