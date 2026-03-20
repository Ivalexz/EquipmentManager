from enum import Enum

class Equipment:
    def __init__(self, id, name, type, weight, model, manufacturer, year, price, location, status):
        self.id = id
        self.name = name
        self.type = type
        self.weight = weight
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.location = location
        self.status = status

class Type(Enum):
    electrical = "Electrical"
    computer = "Computer"
    peripheral = "Peripheral" # принтер, сканер, монітор
    network = "Network" # роутер, кабелі
    furniture = "Furniture"
    audio_video = "Audio/Video"
    other = "Other"

class Status(Enum):
    working = "Working"
    needs_repair = "Needs Repair"
    broken = "Broken"
    in_storage = "In Storage"
    lost = "Lost"