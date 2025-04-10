from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QMenu, QAction
from PyQt6.QtGui import QFont

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()

        tableMenu = menubar.addMenu('Таблицы')
        queryMenu = menubar.addMenu('Запросы')
        aboutMenu = menubar.addMenu('О программе')
        exitMenu = menubar.addMenu('Выход')

        # Пункты меню "Таблицы"
        orderAction = QAction('Заказы', self)
        orderAction.triggered.connect(self.OrderWindow)
        tableMenu.addAction(orderAction)

        managerAction = QAction('Менеджеры', self)
        managerAction.triggered.connect(self.ManagerWindow)
        tableMenu.addAction(managerAction)

        clientAction = QAction('Клиенты', self)
        clientAction.triggered.connect(self.ClientWindow)
        tableMenu.addAction(clientAction)

        # Пункты меню "О программе"
        aboutAction = QAction('About', self)
        aboutAction.triggered.connect(self.AboutWindow)
        aboutMenu.addAction(aboutAction)

        # Пункты меню "Выход"
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        exitMenu.addAction(exitAction)

        self.setGeometry(600, 600, 600, 400)
        self.setWindowTitle('СофаСтрой')
        self.show()

    def OrderWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Таблица заказов")
        new_window.setGeometry(600, 600, 600, 400)
        new_window.exec()

    def ManagerWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Таблица менеджеров")
        new_window.setGeometry(600, 600, 600, 400)
        new_window.exec()

    def ClientWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Таблица клиентов")
        new_window.setGeometry(600, 600, 600, 400)
        new_window.exec()

    def SuppliersWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Поставщики")
        new_window.setGeometry(600, 600, 600, 400)
        new_window.exec()

    def OrdersSumWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Суммы заказов")
        new_window.setGeometry(600, 600, 600, 400)
        new_window.exec()

    def ClientsCountWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Общее количество клиентов")
        new_window.setGeometry(600, 600, 600, 400)
        new_window.exec()

    def AboutWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("О программе")
        new_window.setGeometry(600, 600, 600, 400)
        label = QLabel(new_window)
        font = QFont("Times New Roman", 14)
        label.setFont(font)
        label.setText("\n  О программе\n")

        label2 = QLabel(new_window)
        font2 = QFont("Arial", 11)
        label2.setFont(font2)
        label2.setText("\n\n\n  Программа для строительной компании \"СофаСтрой\".\n"
                       "Цель: удовлетворение клиента строительными материалами и услугами"
                       "Создатель: Арутюнян Софья Кареновна\n"
                       "Программный продукт \"СофаСтройprog\", версия 1.0,\nдля ОС Windows\n"
                       "Телефон для справок: +7(916)-218-97-15 \n"
                       "E-mail: arutynyan.sk@mail.ru"
                       "\n\n\nИздана: 2023.11.11\n"
                       "ООО \"СофаСтрой\" \nКПП +7(916)-218-97-15\n109129, г. Москва, ул. Волгоградский пр-т., 43")

        new_window.exec()

if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    app.exec()
