from enum import Enum


class EquipmentType(str, Enum):
    electrical = "Electrical"
    computer = "Computer"
    peripheral = "Peripheral"
    network = "Network"
    furniture = "Furniture"
    audio_video = "Audio/Video"
    other = "Other"

class EquipmentStatus(str, Enum):
    working = "Working"
    needs_repair = "Needs Repair"
    broken = "Broken"
    in_storage = "In Storage"
    lost = "Lost"

class IssueStatus(str, Enum):
    in_progress = "In Progress"
    resolved = "Resolved"
    not_resolved = "Not Resolved"