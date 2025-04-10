from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Test_ui import Ui_MainWindow
import pandas as pd
import math

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display_result)
        self.pushButton_2.clicked.connect(self.export_to_excel)
        self.show()

    def display_result(self):
        # Получаем значения из текстовых полей
        value_a = float(self.lineEdit.text())
        value_b = float(self.lineEdit_2.text())
        x_min = float(self.lineEdit_3.text())
        x_max = float(self.lineEdit_4.text())
        dx = float(self.lineEdit_5.text())

        # Генерируем данные для таблицы
        data = []
        current_x = x_min
        while current_x <= x_max:
            y = current_x ** 2 - value_a ** 3 - value_b ** 2 * math.sqrt(19 * current_x - 3.5 + math.log(value_a))
            data.append([current_x, y])
            current_x += dx

        # Очищаем таблицу
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)

        # Вставляем данные в таблицу
        for row, row_data in enumerate(data):
            self.tableWidget.insertRow(row)
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

    def export_to_excel(self):
        # Получаем данные из таблицы
        data = []
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text() if item is not None else "")
            data.append(row_data)

        # Создаем DataFrame из данных
        df = pd.DataFrame(data, columns=["X", "Y"])

        # Сохраняем DataFrame в файл Excel
        df.to_excel("output.xlsx", index=False)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    app.exec()

