from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.QtGui import QAction

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

        gameAction = QAction('Игра', self)
        gameAction.triggered.connect(self.GameWindow)
        tableMenu.addAction(gameAction)


        emplAction = QAction('Сотрудники', self)
        emplAction.triggered.connect(self.EmplWindow)
        tableMenu.addAction(emplAction)

        postAction = QAction('Должности', self)
        postAction.triggered.connect(self.PostWindow)
        tableMenu.addAction(postAction)

        facAction = QAction('Средства разработки', self)
        facAction.triggered.connect(self.FacWindow)
        tableMenu.addAction(facAction)

        deveAction = QAction('Разработчик', self)
        deveAction.triggered.connect(self.DeveWindow)
        tableMenu.addAction(deveAction)

        zapopiAction = QAction('Описание игр', self)
        zapopiAction.triggered.connect(self.ZapopiWindow)
        queryMenu.addAction(zapopiAction)

        zapdevAction = QAction('Разработчик игр', self)
        zapdevAction.triggered.connect(self.ZapdevWindow)
        queryMenu.addAction(zapdevAction)

        zaplangAction = QAction('Язык программирования', self)
        zaplangAction.triggered.connect(self.ZaplangWindow)
        queryMenu.addAction(zaplangAction)

        zapsAction = QAction('Заработная плата', self)
        zapsAction.triggered.connect(self.ZapsWindow)
        queryMenu.addAction(zapsAction)

        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        exitMenu.addAction(exitAction)

        aboutWindow = QAction('О программе', self)
        aboutWindow.triggered.connect(self.AboutWindow)
        aboutMenu.addAction(aboutWindow)

        self.setGeometry(500, 500, 500, 400)
        self.setWindowTitle('GameSSS')
        self.show()

    def GameWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Игра")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def EmplWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Сотрудники")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def PostWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Должности")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def FacWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Средства разработки")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def DeveWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Разработчик")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def ZapopiWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Описание игр")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def ZapdevWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Разработчик игр")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def ZaplangWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Язык программирования")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def ZapsWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("Зааботная плата")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()

    def AboutWindow(self):
        new_window = QDialog()
        new_window.setWindowTitle("О программе")
        new_window.setGeometry(500, 500, 500, 400)
        new_window.exec()



if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    app.exec()
