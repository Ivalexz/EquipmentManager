import datetime
from models.EquipmentMovesHistory import EquipmentMovesHistory

class MoveHistoryService:
    def __init__(self, equipment_service):
        self.move_history_list =[]
        self.equipment_service = equipment_service

    def get_all_move_history(self):
        return self.move_history_list

    def get_move_history_by_equipment_id(self, equipment_id):
        result = None
        for move in self.move_history_list:
            if move.equipment_id == equipment_id:
                result = move
                break
        return result

    def move_equipment(self, equipment_id, new_location):
        eq = self.equipment_service.get_equipment_by_id(equipment_id)
        if eq is None:
            return None

        old_location = eq.location
        eq.location = new_location

        new_move = EquipmentMovesHistory(id=len(self.move_history_list) + 1,
            equipment_id=equipment_id,
            from_location=old_location,
            to_location=new_location,
            move_date=datetime.datetime.utcnow().isoformat()
        )
        self.move_history_list.append(new_move)
        return new_move