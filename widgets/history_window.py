from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLabel
import requests


class HistoryWindow(QWidget):
    def __init__(self, equipment_id):
        super().__init__()
        self.equipment_id = equipment_id
        self.url = "http://127.0.0.1:8000"

        self.setWindowTitle("Історія змін")
        self.setFixedSize(400, 300)

        self.history_table=QTableWidget(self)
        self.history_table.setColumnCount(5)
        self.history_table.setHorizontalHeaderLabels(["ID", "ID обладнання", "Звідки", "Куди", "Дата"])
        self.history_table.move(10, 10)
        self.history_table.resize(380, 280)


        self.close_btn=QPushButton("Закрити", self)
        self.close_btn.move(150, 260)
        self.close_btn.resize(100, 30)
        self.close_btn.clicked.connect(self.hide)

        self.load_history()

    def fill_history(self, history_data):
        self.history_table.setRowCount(len(history_data))
        for row_idx, move in enumerate(history_data):
            self.history_table.setItem(row_idx, 0, QTableWidgetItem(str(move["id"])))
            self.history_table.setItem(row_idx, 1, QTableWidgetItem(str(move["equipment_id"])))
            self.history_table.setItem(row_idx, 2, QTableWidgetItem(move["from_location"]))
            self.history_table.setItem(row_idx, 3, QTableWidgetItem(move["to_location"]))
            self.history_table.setItem(row_idx, 4, QTableWidgetItem(move["move_date"]))


    def load_history(self):
        try:
            resp = requests.get(f"{self.url}/move_history/equipment/{self.equipment_id}")
            data = resp.json()
            self.fill_history(data)
            self.show()
        except Exception as e:
            print("Помилка:", e)