from enum import Enum


class EquipmentType(Enum):
    electrical = "Electrical"
    computer = "Computer"
    peripheral = "Peripheral" # принтер, сканер, монітор
    network = "Network" # роутер, кабелі
    furniture = "Furniture"
    audio_video = "Audio/Video"
    other = "Other"

class EquipmentStatus(Enum):
    working = "Working"
    needs_repair = "Needs Repair"
    broken = "Broken"
    in_storage = "In Storage"
    lost = "Lost"

class IssueStatus(Enum):
    in_progress = "In Progress"
    resolved = "Resolved"
    not_resolved = "Not Resolved"