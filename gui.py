from PySide6 import QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QWidget
# from tasks import Tasks


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyTasks")
        self.setMinimumSize(QSize(400, 300))
        # task1 = Tasks()
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
        self.lne_task_name.setMaxLength(30)
        self.lne_task_name.setPlaceholderText("Ajouter une tache")
        self.btn_del_task = QPushButton("Tout supprimer")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_Layout = QVBoxLayout()

    def add_widgets_to_layouts(self):
        self.main_Layout.addWidget(self.lst_tasks)
        self.main_Layout.addWidget(self.lne_task_name)
        self.main_Layout.addWidget(self.btn_del_task)

    def setup_connections(self):
        self.lne_task_name.returnPressed.connect(self.add_task)
        self.btn_del_task.clicked.connect(self.delete_all_task)
        self.lst_tasks.itemDoubleClicked.connect(self.delete_task)

    def add_task(self):
        self.lst_tasks.addItem(self.lne_task_name.text())
        self.lne_task_name.clear()

    def delete_all_task(self):
        self.lst_tasks.clear()

    def delete_task(self, item):
        self.lst_tasks.takeItem(self.lst_tasks.row(item))


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
