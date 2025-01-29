import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QWidget,QApplication,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import Qt 
from controllers.authController import AuthController

class LoginUi(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.auth_Controller = AuthController()
        # self.setStyleSheet("background-color:#2ECC7100;")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.firstNameLabel = QLineEdit("")
        self.firstNameLabel.setFixedWidth(250)
        self.setStyleSheet("""
QLineEdit{background-color:white;padding:10px;border:1px solid;border-radius:5px;color:black;}
QPushButton{background-color:orange;color:black;border:0px solid;border-radius:5px;padding:5px}
QPushButton::hover{background-color:green;}
""")
        self.firstNameLabel.setPlaceholderText("Enter your first name")
        self.firstNameLabel.setFont(QFont("Times",14))

        self.lastNameLabel = QLineEdit("")
        self.lastNameLabel.setFixedWidth(250)
        self.lastNameLabel.setPlaceholderText("Enter your last name")
        self.lastNameLabel.setFont(QFont("Times",14))

        self.emailLabel = QLineEdit("")
        self.emailLabel.setFixedWidth(250)
        self.emailLabel.setPlaceholderText("Enter your email")
        self.emailLabel.setFont(QFont("Times",14))

        self.passwordLabel = QLineEdit("")
        self.passwordLabel.setFixedWidth(250)
        self.passwordLabel.setPlaceholderText("Enter your password")
        self.passwordLabel.setFont(QFont("Times",14))
        self.passwordLabel.setEchoMode(QLineEdit.EchoMode.Password)

        self.registerButton = QPushButton("Register")
        self.registerButton.clicked.connect(self.handleRegister)
        self.registerButton.setFont(QFont("Times",14))
        self.registerButton.setFixedWidth(250)

        form_layout.addWidget(self.firstNameLabel)
        form_layout.addWidget(self.lastNameLabel)
        form_layout.addWidget(self.emailLabel)
        form_layout.addWidget(self.passwordLabel)
        form_layout.addWidget(self.registerButton)

        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def handleRegister(self):
        firstName = self.firstNameLabel.text()
        lastName = self.lastNameLabel.text()
        email = self.emailLabel.text()
        password = self.passwordLabel.text()

        try:
            success,message=self.auth_Controller.signUp(firstName, lastName, email, password)
            if success:
                QMessageBox.information(self, "Registration Successful", message)
                self.close()
            else:
                QMessageBox.warning(self, "Registration Failed", message)
            print("Registration successful")
        except Exception as e:
            print(f"Registration failed: {str(e)}")
        

app = QApplication([])
window = LoginUi()
window.show()
app.exec()