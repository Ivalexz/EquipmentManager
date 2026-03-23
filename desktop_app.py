import sys
from PyQt6.QtWidgets import QApplication
from widgets.app import App

ui_app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(ui_app.exec())