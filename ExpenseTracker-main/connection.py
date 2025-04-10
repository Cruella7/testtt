
from PySide6 import QtWidgets, QtSql


class Data:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Data, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec_("""
            CREATE TABLE IF NOT EXISTS users (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username VARCHAR(20),
                Password VARCHAR(20)
            );
        """)

        query.exec_("""
            CREATE TABLE IF NOT EXISTS expenses (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Date VARCHAR(20),
                Category VARCHAR(20),
                Description VARCHAR(20),
                Balance REAL,
                Status VARCHAR(20),
                UserID INTEGER,
                FOREIGN KEY (UserID) REFERENCES users(ID)
            );
        """)
        return True

    def if_user(self, username):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT id FROM users WHERE username = :username")
        query.bindValue(':username', username)
        query.exec_()

        if query.next():
            return True

    def add_user(self, username, password):
        query = QtSql.QSqlQuery()
        query.prepare("INSERT INTO users (Username, Password) VALUES (:username, :password)")
        query.bindValue(':username', username)
        query.bindValue(':password', password)

        if query.exec_():
            print("User added successfully.")
        else:
            print("Error adding user:", query.lastError().text())

    def get_users(self):
        query = QtSql.QSqlQuery()
        query.exec_("SELECT ID, Username, Password FROM users")

        results = []
        while query.next():
            user_id = query.value(0)
            username = query.value(1)
            password = query.value(2)
            results.append((user_id, username, password))

        return results

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")

    def total_income(self):
        return self.get_total(column="Balance", filter="Status", value="Income")

    def total_outcome(self):
        return self.get_total(column="Balance", filter="Status", value="Outcome")

    def total_groceries(self):
        return self.get_total(column="Balance", filter="Category", value="Grocery")

    def total_auto(self):
        return self.get_total(column="Balance", filter="Category", value="Auto")

    def total_entertainment(self):
        return self.get_total(column="Balance", filter="Category", value="Entertainment")

    def total_other(self):
        return self.get_total(column="Balance", filter="Category", value="Other")
