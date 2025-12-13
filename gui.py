from PySide6 import QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyTasks")
        self.setMinimumSize(QSize(400, 300))
        # Initialisation de l'UI
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_Layout)
        self.setCentralWidget(self.central_widget)
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lst_tasks = QListWidget()
        self.lne_task_name = QLineEdit()
        self.btn_add_task = QPushButton("tout supprimer")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_Layout = QVBoxLayout()

    def add_widgets_to_layouts(self):
        self.main_Layout.addWidget(self.lst_tasks)
        self.main_Layout.addWidget(self.lne_task_name)
        self.main_Layout.addWidget(self.btn_add_task)

    def setup_connections(self):
        pass


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
