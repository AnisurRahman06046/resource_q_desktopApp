from PyQt6.QtWidgets import QMainWindow,QApplication

from ui.signup import SignUpWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resource Quest")
        self.setGeometry(500, 200, 1074, 718)
        self.setStyleSheet("QWidget{background-color:#e0e7ff}")
        self.load_ui()

    def load_ui(self):
        self.signup_window = SignUpWindow()
        self.signup_window.setupUi(self)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()