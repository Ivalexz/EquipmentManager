import requests
from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout


class App(QWidget):
    def __init__(self):
        self.url = "http://127.0.0.1:8000"
        self.init_ui()

    def start_ui(self):
       pass

    def load_equipment(self):
        pass

    def fill_table(self, data):
       pass