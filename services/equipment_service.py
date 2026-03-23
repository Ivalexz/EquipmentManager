from models.Equipment import Equipment
from models.enums import EquipmentType, EquipmentStatus


class EquipmentService:
    def __init__(self):
        self.equipment_list = [
            Equipment(
                id=1,
                name="Принтер HP",
                type=EquipmentType.peripheral,
                model="LaserJet 1020",
                manufacturer="HP",
                year=2023,
                price=5000.0,
                location="101",
                status=EquipmentStatus.working
            ),
            Equipment(
                id=2,
                name="Ноутбук Dell",
                type=EquipmentType.computer,
                model="Inspiron 15",
                manufacturer="Dell",
                year=2022,
                price=25000.0,
                location="102",
                status=EquipmentStatus.working
            ),
            Equipment(
                id=3,
                name="Монітор Samsung",
                type=EquipmentType.peripheral,
                model="S24F350",
                manufacturer="Samsung",
                year=2021,
                price=7000.0,
                location="103",
                status=EquipmentStatus.needs_repair
            )
        ]

    def get_all_equipment(self):
        return self.equipment_list

    def get_equipment_by_id(self, equipment_id):
        item_res=None
        for item in self.equipment_list:
            if item.id == equipment_id:
                item_res=item
                break
        return item_res

    def add_equipment(self, equipment):
        if self.get_equipment_by_id(equipment.id):
            return None
        self.equipment_list.append(equipment)
        return equipment

    def update_status(self, equipment_id, new_status):
        for index, eq in enumerate(self.equipment_list):
            if eq.id == equipment_id:
                eq.status = new_status
                return self.equipment_list[index]
        return None
