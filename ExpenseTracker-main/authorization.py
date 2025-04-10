import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_authorization import Ui_Authorization  # Импортируйте ваш созданный модуль
from connection import Data
from regist import RegistrationWindow



class AuthorizationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.conn = Data()
        self.ui.pushButton_5.clicked.connect(self.Enter)
        self.ui.pushButton_6.clicked.connect(self.Registr)


    def check_login(self, username, password):
        users = self.conn.get_users()

        for user_id, stored_username, stored_password in users:
            if stored_username == username and stored_password == password:
                print(f"Login successful for user with ID {user_id}.")
                return True

        self.ui.label.setStyleSheet("color: red; font-size: 12pt;")
        self.ui.label.setText("Не верный логин или пароль")
        print("Incorrect username or password.")
        return False

    def Enter(self):
        if self.check_login(self.ui.lineEdit_5.text(), self.ui.lineEdit_6.text()):
            self.hide()
            self.flag = True


    def closeEvent(self, event):
        # Дополнительные действия перед закрытием окна
        print("Closing...")
        super().closeEvent(event)

    def Registr(self):
        registration_window = RegistrationWindow()
        registration_window.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = AuthorizationDialog()
    dialog.show()
    sys.exit(app.exec())
