import requests
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QPushButton, QTableWidget, QTableWidgetItem
from models.enums import EquipmentStatus
from widgets.history_window import HistoryWindow
from widgets.tech_issues_window import TechIssuesWindow


class App(QWidget):
    def __init__(self):
        super().__init__()  # запускає конструктор QWidget
        self.url = "http://127.0.0.1:8000"
        self.start_ui()

    def start_ui(self):  # створення і розміщення віджетів
        self.setWindowTitle("Облік обладнання")
        self.setFixedSize(1000, 700)

        self.input_equipment_name = QLineEdit("Пошук за назвою...", self)
        self.input_equipment_name.move(10, 50)
        self.input_equipment_name.resize(220, 30)

        self.filter_combo = QComboBox(self)
        self.filter_combo.addItem("Усі")
        for status in EquipmentStatus:
            self.filter_combo.addItem(status.value)
        self.filter_combo.move(250, 50)
        self.filter_combo.resize(160, 30)

        self.load_list_btn = QPushButton("Завантажити список", self)
        self.load_list_btn.move(430, 50)
        self.load_list_btn.resize(160, 30)

        self.save_file_btn = QPushButton("Зберегти в файл", self)
        self.save_file_btn.move(610, 50)
        self.save_file_btn.resize(160, 30)

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Назва", "Тип", "Кабінет", "Стан", "Рік випуску"])
        self.table.move(10, 80)
        self.table.resize(980, 320)

        self.input_eq_id = QLineEdit("ID обладнання...", self)
        self.input_eq_id.move(10, 430)
        self.input_eq_id.resize(100, 30)

        self.state_combo = QComboBox(self)
        for status in EquipmentStatus:
            self.state_combo.addItem(status.value)
        self.state_combo.move(130, 430)
        self.state_combo.resize(150, 30)

        self.update_status_btn = QPushButton("Оновити статус", self)
        self.update_status_btn.move(300, 430)
        self.update_status_btn.resize(130, 30)

        self.input_room = QLineEdit("Новий кабінет...", self)
        self.input_room.move(450, 430)
        self.input_room.resize(130, 30)

        self.move_btn = QPushButton("Перемістити", self)
        self.move_btn.move(600, 430)
        self.move_btn.resize(120, 30)

        self.history_btn = QPushButton("Історія переміщень", self)
        self.history_btn.move(10, 480)
        self.history_btn.resize(180, 30)

        self.tech_issues_btn = QPushButton("Технічні проблеми", self)
        self.tech_issues_btn.move(210, 480)
        self.tech_issues_btn.resize(180, 30)

        self.load_list_btn.clicked.connect(self.load_equipment)
        self.update_status_btn.clicked.connect(self.update_status)
        self.move_btn.clicked.connect(self.move_equipment)
        self.history_btn.clicked.connect(self.show_history)
        self.tech_issues_btn.clicked.connect(self.show_tech_issues)

        self.save_file_btn.clicked.connect(self.save_to_file)

    def load_equipment(self):    #запити до апі та передавання даних
        try:
            resp = requests.get(f"{self.url}/equipment")
            data = resp.json()
            self.data_now = data
            self.fill_table(data)
        except Exception as e:
            print("Помилка при завантаженні даних:", e)

    def fill_table(self, data):    # відображення даних в таблиці
        self.table.setRowCount(len(data))
        for row, item in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.table.setItem(row, 1, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 2, QTableWidgetItem(item["type"]))
            self.table.setItem(row, 3, QTableWidgetItem(item["location"]))
            self.table.setItem(row, 4, QTableWidgetItem(item["status"]))
            self.table.setItem(row, 5, QTableWidgetItem(item["year"]))

    def save_to_file(self):
        data = self.data_now
        try:
            with open("equipment_list.txt", "w") as file:
                for item in data:
                    file.write(f"{item['id']} - {item['name']} - {item['type']} - {item['location']} - {item['status']} - {item['year']}\n")
            print("Дані збережено в equipment_list.txt")
        except Exception as e:
            print("Помилка при збереженні в файл:", e)

    def update_status(self):
        eq_id = self.input_eq_id.text()
        new_status = self.state_combo.currentText()
        try:
            requests.patch(f"{self.url}/equipment/{eq_id}/status",
                           params={"new_status": new_status})
        except Exception as e:
            print("Помилка при оновленні статусу:", e)

    def move_equipment(self):
        eq_id = self.input_eq_id.text()
        new_room = self.input_room.text()
        try:
            requests.post(f"{self.url}/move_history/move",
                          params={"equipment_id": eq_id, "new_location": new_room})
        except Exception as e:
            print("Помилка при переміщенні обладнання:", e)

    def show_history(self):
        eq_id = self.input_eq_id.text()
        self.h_w=HistoryWindow(eq_id)

    def show_tech_issues(self):
        self.t_i_w=TechIssuesWindow()
        self.t_i_w.load_issues()