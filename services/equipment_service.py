from models import Equipment

class EquipmentService:
    def __init__(self):
        self.equipment_list=[]

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
