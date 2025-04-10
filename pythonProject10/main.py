import sys
from PyQt6.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt6 import uic
import sqlite3
from PyQt6.QtWidgets import *
import csv


class User:
    def __init__(self):
        self.is_auth = False
        self.data = None



class Vhod(QMainWindow):

    def __init__(self):
        super().__init__()
        # Загрузка пользовательского интерфейса из файла 'interface.ui'
        uic.loadUi('newvhod.ui', self)
        #Соединение сигнала "clicked" кнопки pushButton_2 с методом show_admin_window
        self.pushButton_2.clicked.connect(self.openPravila)
        #Соединение сигнала "clicked" кнопки pushButton с методом show_minds_window
        self.pushButton.clicked.connect(self.openRegis)

    def openRegis(self):
        regis.show()
        self.close()

    def openPravila(self):
        pravila.show()

class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка пользовательского интерфейса из файла 'Adminn.ui'
        uic.loadUi('registrationnew.ui', self)
        # Соединение сигнала "clicked" кнопки vxod с методом auth
        self.pushButton.clicked.connect(self.auth)
        self.backButton.clicked.connect(self.go_back)
        self.is_auth = False
        # Определение метода для аутентификации администратора.

    def auth(self):
        # Получение введенного логина из виджета login и password
        lineEdit = self.lineEdit.text()
        lineEdit_2 = self.lineEdit_2.text()
        # Берём информцию об админах из БД
        cursor.execute('SELECT login, password FROM admins')
        admins = cursor.fetchall()
        # Берём информцию о пассажирах из БД
        cursor.execute('SELECT login, password FROM passengers')
        passengers = cursor.fetchall()
        # Система атризации с проверкой
        if lineEdit in [login for login, password in admins]:
            for login, password in admins:
                if lineEdit == login and lineEdit_2 == password:
                    data = cursor.execute(f'SELECT * FROM admins WHERE login="{login}"').fetchall()
                    user.is_auth = True
                    user.data = data[0]
                    admin.hello_name = f'{user.data[0]} {user.data[1]}'
                    admin.set_name()
                    admin.show()
                    self.close()
                    break
            else:
                QMessageBox.critical(self, 'Ошибка', 'Неверный логин или пароль')
        elif lineEdit in [login for login, password in passengers]:
            for login, password in passengers:
                if lineEdit == login and lineEdit_2 == password:
                    data = cursor.execute(f'SELECT * FROM passengers WHERE login="{login}"').fetchall()
                    user.is_auth = True
                    user.data = data[0]
                    passengerLC.hello_name = f'{user.data[0]} {user.data[1]}'
                    passengerLC.set_name()
                    passengerLC.show()
                    self.close()
                    break
            else:
                QMessageBox.critical(self, 'Ошибка', 'Неверный логин или пароль')
        else:
            QMessageBox.critical(self, 'Ошибка', 'Такого пользователя не существует')


    def go_back(self):
        newvhod.show()
        self.close()


class Praila(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка пользовательского интерфейса из файла
        uic.loadUi('pravila.ui', self)

class AdminLC(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка пользовательского интерфейса из файла
        uic.loadUi('adminLC.ui', self)
        # Соединение сигнала "clicked" с кнопками
        self.data_btn.clicked.connect(self.table_admin_info)
        self.pass_btn.clicked.connect(self.table_passen)
        self.air_btn.clicked.connect(self.table_airs)
        self.rasp_btn.clicked.connect(self.table_airs)
        self.upload_btn.clicked.connect(self.download_file)
        self.id_del = -1

        self.hello_name = None

        # Вызов метода table_view для отображения данных в таблице при инициализации окна
        self.table_airs()

    def set_name(self):
        self.hello_label.setText(f'{self.hello_label.text()} {self.hello_name}')

    def table_admin_info(self):
        # Устанавливаем соединение с базой данных
        cursor.execute('SELECT * FROM admins')
        # Получаем все записи из результата запроса.
        admins = cursor.fetchall()
        # Устанавливаем количество строк в таблице равным количеству записей в базе данных.
        self.tableWidget.setRowCount(len(admins))
        # Устанавливаем количество столбцов в таблице равным 1.
        self.tableWidget.setColumnCount(5)
        # Отключаем возможность редактирования ячеек таблицы.
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        # Проставляем столбцы
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Имя'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Фамилия'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Возраст'))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('Логин'))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('Пароль'))
        # Заполняем таблицу
        x = 0
        for name in admins:
            for i in range(5):
                self.tableWidget.setItem(x, i, QTableWidgetItem(name[i]))
            x += 1

    def table_passen(self):
        # Устанавливаем соединение с базой данных
        cursor.execute('SELECT * FROM passengers')
        # Получаем все записи из результата запроса.
        passengersss = cursor.fetchall()
        # Устанавливаем количество строк в таблице равным количеству записей в базе данных.
        self.tableWidget.setRowCount(len(passengersss))
        # Устанавливаем количество столбцов в таблице равным 1.
        self.tableWidget.setColumnCount(1)
        # Отключаем возможность редактирования ячеек таблицы.
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Наши пассажиры'))
        x = 0
        # Заполняем таблицу

        for name in passengersss:
            self.tableWidget.setItem(x, 0, QTableWidgetItem(f'{name[1]} {name[0]} {name[2]}, {name[3]}'))
            x += 1

    def table_airs(self):
        # Устанавливаем соединение с базой данных
        cursor.execute('SELECT * FROM reisi')
        # Получаем все записи из результата запроса.
        air = cursor.fetchall()
        # Устанавливаем количество строк в таблице равным количеству записей в базе данных.
        self.tableWidget.setRowCount(len(air))
        # Устанавливаем количество столбцов в таблице равным 1.
        self.tableWidget.setColumnCount(6)
        # Отключаем возможность редактирования ячеек таблицы.
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        # Проставляем столбцы
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Номер рейса'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Откуда'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Куда'))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('Отправление'))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('Прибытие'))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem('Время пути'))
        # Заполняем таблицу

        x = 0
        for flight in air:
            for i in range(1, 7):
                self.tableWidget.setItem(x, i-1, QTableWidgetItem(str(flight[i])))
            x += 1

    def download_file(self):
        cursor.execute('SELECT * FROM reisi')
        # Получаем все записи из результата запроса.
        air = cursor.fetchall()
        # Выбор папки и запись пути в переменную
        file = QFileDialog.getExistingDirectory(self,"Выбрать папку",".") + '/res.csv'
        # Открытие CSV файла и заполнение данными
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['Номер', 'Откуда', 'Куда', 'Отправление', 'Прибытие', 'Время пути']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for i in air:
                writer.writerow({'Номер': i[1], 'Откуда': i[2], 'Куда': i[3],
                                 'Отправление': i[4], 'Прибытие': i[5], 'Время пути': i[6]})

            csvfile.close()
        # Диалоговое окно с информацией о выгрузке файла
        message = QMessageBox()

        message.setWindowTitle('Информация')
        message.setText('Ваш файл выгружен')
        message.exec()


class PassengerLCK(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка пользовательского интерфейса из файла
        uic.loadUi('passengerLCK.ui', self)

        # Соединение сигнала "clicked" с кнопками
        self.pushButton_2.clicked.connect(self.table_poezdki)
        self.pushButton_3.clicked.connect(self.table_moneti)
        self.pushButton_4.clicked.connect(self.table_broni)
        self.pushButton.clicked.connect(self.table_online)

        self.id_del = -1
        self.hello_name = None
        # Вызов метода table_view для отображения данных в таблице при инициализации окна

        cursor.execute('SELECT name, surname FROM passengers')
        name, surname = cursor.fetchall()[0]


    def set_name(self):
        self.label_2.setText(f'{self.label_2.text()} {self.hello_name}')

    def table_poezdki(self):
        # Устанавливаем соединение с базой данных
        cursor.execute(f'SELECT my_air FROM passengers WHERE login="{user.data[7]}"')
        # Получаем все записи из результата запроса.
        poezdki = cursor.fetchall()[0][0].split(', ')
        # Устанавливаем количество строк в таблице равным количеству записей в базе данных.
        self.tableWidget.setRowCount(len(poezdki))
        # Устанавливаем количество столбцов в таблице равным 1.
        self.tableWidget.setColumnCount(1)
        # Отключаем возможность редактирования ячеек таблицы.
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Мои поезди'))

        x = 0
        for item in poezdki:
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(item)))
            x += 1

    def table_moneti(self):
        # Устанавливаем соединение с базой данных
        cursor.execute(f'SELECT moneti FROM passengers WHERE login="{user.data[7]}"')
        # Получаем все записи из результата запроса.
        moneti = cursor.fetchall()
        # Устанавливаем количество строк в таблице равным количеству записей в базе данных.
        self.tableWidget.setRowCount(len(moneti))
        # Устанавливаем количество столбцов в таблице равным 1.
        self.tableWidget.setColumnCount(1)
        # Отключаем возможность редактирования ячеек таблицы.
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Мои монеты'))
        # Заполняем таблицу

        x = 0
        for name in moneti:
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(name[0])))
            x += 1

    def table_broni(self):
        # Устанавливаем соединение с базой данных
        cursor.execute(f'SELECT my_broni FROM passengers WHERE login="{user.data[7]}"')
        # Получаем все записи из результата запроса.
        my_broni = cursor.fetchall()[0][0].split(', ')

        # Устанавливаем количество строк в таблице равным количеству записей в базе данных.
        self.tableWidget.setRowCount(len(my_broni))
        # Устанавливаем количество столбцов в таблице равным 1.
        self.tableWidget.setColumnCount(1)
        # Отключаем возможность редактирования ячеек таблицы.
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Мои поезди'))
        # Заполняем таблицу

        x = 0
        for item in my_broni:
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(item)))
            x += 1

    def table_online(self):
        newvhod.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    user = User()

    newvhod = Vhod()
    regis = Registration()
    pravila = Praila()
    newvhod.show()

    passengerLC = PassengerLCK()
    admin = AdminLC()


    sys.exit(app.exec())
