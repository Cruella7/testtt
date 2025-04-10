import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QDialog, QMessageBox
import sqlite3


class AuthorizationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Authorization")
        self.setGeometry(200, 200, 300, 150)

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        self.status = None

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
        conn.close()

        if user:
            self.accept()
            self.status = user[3]
        else:
            QMessageBox.warning(self, "Login Error", "Invalid username or password!")


class AddPairWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Pair")
        self.setGeometry(200, 200, 400, 200)

        self.date_label = QLabel("Date:")
        self.date_input = QLineEdit()

        self.teacher_label = QLabel("Teacher:")
        self.teacher_input = QLineEdit()

        self.group_label = QLabel("Group:")
        self.group_input = QLineEdit()

        self.subject_label = QLabel("Subject:")
        self.subject_input = QLineEdit()

        self.submit_button = QPushButton("Add Pair")
        self.submit_button.clicked.connect(self.add_pair)

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.teacher_label)
        layout.addWidget(self.teacher_input)
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_input)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def add_pair(self):
        date = self.date_input.text()
        teacher = self.teacher_input.text()
        group = self.group_input.text()
        subject = self.subject_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pairs (date, teacher, group_name, subject) VALUES (?, ?, ?, ?)",
                       (date, teacher, group, subject))
        conn.commit()
        conn.close()

        self.close()


class ScheduleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schedule")
        self.setGeometry(200, 200, 600, 400)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Date", "Teacher", "Group", "Subject"])

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_schedule(self):
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pairs")
        pairs = cursor.fetchall()
        conn.close()

        self.table.setRowCount(0)  # Clear existing rows

        for row_num, pair in enumerate(pairs):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(pair):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))


class TeacherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pair Scheduler")
        self.setGeometry(200, 200, 600, 400)

        self.add_pair_button = QPushButton("Add Pair")
        self.add_pair_button.clicked.connect(self.open_add_pair_window)

        self.view_schedule_button = QPushButton("View Schedule")
        self.view_schedule_button.clicked.connect(self.open_schedule_window)

        layout = QVBoxLayout()
        layout.addWidget(self.add_pair_button)
        layout.addWidget(self.view_schedule_button)

        self.schedule_window = ScheduleWindow()
        layout.addWidget(self.schedule_window)

        self.setLayout(layout)

    def open_add_pair_window(self):
        add_pair_window = AddPairWindow()
        add_pair_window.exec_()

    def open_schedule_window(self):
        self.schedule_window.load_schedule()


class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pair Scheduler")
        self.setGeometry(200, 200, 600, 400)

        self.view_schedule_button = QPushButton("View Schedule")
        self.view_schedule_button.clicked.connect(self.open_schedule_window)

        layout = QVBoxLayout()
        layout.addWidget(self.view_schedule_button)

        self.schedule_window = ScheduleWindow()
        layout.addWidget(self.schedule_window)

        self.setLayout(layout)

    def open_schedule_window(self):
        self.schedule_window.load_schedule()


if __name__ == '__main__':

    conn = sqlite3.connect('pairs_users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    user_type TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pairs
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    teacher TEXT,
                    group_name TEXT,
                    subject TEXT)''')
    conn.commit()
    conn.close()

    app = QApplication(sys.argv)
    TeacherWindow = TeacherApp()
    StudentWindow = StudentApp()

    authorization_window = AuthorizationWindow()
    if authorization_window.exec_() == QDialog.Accepted:
        if authorization_window.status == 'student':
            StudentWindow.show()
        else:
            TeacherWindow.show()
    
    sys.exit(app.exec_())
