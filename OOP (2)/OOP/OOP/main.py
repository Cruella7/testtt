from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QMessageBox, QInputDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Установка свойств окна
        self.setWindowTitle("Программа для просмотра данных")
        self.setGeometry(100, 100, 961, 802)

        # Настройка центрального виджета и его компоновки
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

        # Добавление метки для меню
        self.label_menu = QLabel("Меню", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(36)
        self.label_menu.setFont(font)
        self.central_layout.addWidget(self.label_menu)

        # Добавление кнопок для различных функциональностей
        self.ButtonAbout = QPushButton("О программе")
        self.ButtonAbout.clicked.connect(self.about)
        self.central_layout.addWidget(self.ButtonAbout)

        self.ButtonDisplayAuthor = QPushButton("Выход")
        self.ButtonDisplayAuthor.clicked.connect(self.close)
        self.central_layout.addWidget(self.ButtonDisplayAuthor)

        self.ButtonDisplayReader = QPushButton("Просмотр данных")
        self.ButtonDisplayReader.clicked.connect(self.view_data)
        self.central_layout.addWidget(self.ButtonDisplayReader)

        self.ButtonEdit = QPushButton("Удалить")
        self.ButtonEdit.clicked.connect(self.delete_row)
        self.central_layout.addWidget(self.ButtonEdit)

        self.tableWidget = QTableWidget()
        self.central_layout.addWidget(self.tableWidget)

    # Метод для отображения данных в таблице
    def view_data(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)

        try:
            with open('inn.txt', 'r', encoding='cp1251') as f_in:
                for row, line in enumerate(f_in):
                    data = line.strip().split(';')
                    print("Data read from file:", data)  # Отладочный вывод
                    self.tableWidget.setRowCount(row + 1)  # Увеличиваем количество строк на 1
                    self.tableWidget.setColumnCount(len(data))  # Устанавливаем количество столбцов
                    for col, item in enumerate(data):
                        self.tableWidget.setItem(row, col, QTableWidgetItem(item))
        except FileNotFoundError:
            QMessageBox.critical(self, "Ошибка", "Файл inn.txt не найден.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при чтении файла: {e}")

    # Метод для удаления строки из таблицы
    def delete_row(self):
        # Очистка таблицы
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)

        # Вывод содержимого файла в таблицу
        try:
            with open('inn.txt', 'r', encoding='cp1251') as f_in:
                for row, line in enumerate(f_in):
                    data = line.strip().split(';')
                    self.tableWidget.insertRow(row)
                    for col, item in enumerate(data):
                        self.tableWidget.setItem(row, col, QTableWidgetItem(item))
        except FileNotFoundError:
            QMessageBox.critical(self, "Ошибка", "Файл inn.txt не найден.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при чтении файла: {e}")

        # Запрос номера строки для удаления
        row_number, ok = QInputDialog.getInt(self, 'Удаление строки', 'Введите номер строки для удаления:')
        if ok:
            # Удаление строки, если пользователь подтверждает выбор
            self.tableWidget.removeRow(row_number)

    # Метод для отображения информации о программе
    def about(self):
        QMessageBox.about(self, "О программе", "Это программа для просмотра данных об автобусах, рейсах и пассажирах")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
