from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLabel
import requests


class TechIssuesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.url= "http://127.0.0.1:8000"

        self.setWindowTitle("Технічні проблеми")
        self.setFixedSize(400, 300)

        self.issues_table = QTableWidget(self)
        self.issues_table.setColumnCount(5)
        self.issues_table.setHorizontalHeaderLabels(["ID", "ID обладнання", "Опис", "Дата", "Статус"])
        self.issues_table.move(10, 10)
        self.issues_table.resize(380, 280)

        self.close_btn = QPushButton("Закрити", self)
        self.close_btn.move(150, 260)
        self.close_btn.resize(100, 30)
        self.close_btn.clicked.connect(self.hide)

    def fill_issues(self, issues_data):
        self.issues_table.setRowCount(len(issues_data))
        for row_idx, issue in enumerate(issues_data):
            self.issues_table.setItem(row_idx, 0, QTableWidgetItem(str(issue["issue_id"])))
            self.issues_table.setItem(row_idx, 1, QTableWidgetItem(str(issue["eq_id"])))
            self.issues_table.setItem(row_idx, 2, QTableWidgetItem(issue["description"]))
            self.issues_table.setItem(row_idx, 3, QTableWidgetItem(issue["issue_date"]))
            self.issues_table.setItem(row_idx, 4, QTableWidgetItem(issue["status"]))

    def load_issues(self):
        try:
            resp = requests.get(f"{self.url}/tech_issues")
            data = resp.json()
            self.fill_issues(data)
            self.show()
        except Exception as e:
            print("Помилка:", e)