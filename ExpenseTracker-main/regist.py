import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_registration import Ui_Regist  # Подключение вашего файла ui_regist.py
from connection import Data


class RegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Инициализация пользовательского интерфейса из файла ui_regist.py
        self.ui = Ui_Regist()
        self.ui.setupUi(self)
        self.conn = Data()
        self.ui.pushButton.clicked.connect(self.regist)

    def regist(self):
        username = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit.text()
        password_confirm = self.ui.lineEdit_3.text()
        print(username, password, password_confirm)

        if self.conn.if_user(username):
            self.ui.label_5.setText("Такой пользователь уже существует.")
        elif password != password_confirm:
            self.ui.label_5.setText("Пароли не совпадают.")
        else:
            self.conn.add_user(username, password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AssertionError()
    win
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec())
