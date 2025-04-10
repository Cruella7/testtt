import sqlite3

# Создаем подключение к базе данных (или создаем новую, если она не существует
connection = sqlite3.connect("mydatabase.db")

# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()
cursor: cursor = connection.cursor()

# Создаем таблицу "Game"
cursor.execute('''CREATE TABLE IF NOT EXISTS Game (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INT NOT NULL, person INT NOT NULL, reiting INT NOT NULL)''')

# Создаем таблицу"Developer"
cursor.execute('''CREATE TABLE IF NOT EXISTS Developer ( id INTEGER PRIMARY KEY, country TEXT NOT NULL, company TEXT NOT NULL, emaill TEXT NOT NULL, price TEXT NOT NULL, inn INT NOT NULL, number INT NOT NULL)''')

# Создаем таблицу"Development tools"
cursor.execute('''CREATE TABLE IF NOT EXISTS Development_tools (id INTEGER PRIMARY KEY,language TEXT NOT NULL, datebase TEXT NOT NULL, engine TEXT NOT NULL)''')

# Создаем таблицу"Post"
cursor.execute('''CREATE TABLE IF NOT EXISTS Post (id INTEGER PRIMARY KEY, salaru INT NOT NULL,  grafic TEXT NOT NULL, name TEXT NOT NULL, responsibilities TEXT NOT NULL )''')

# Создаем таблицу"Worker"
cursor.execute('''CREATE TABLE IF NOT EXISTS Worker (id INTEGER PRIMARY KEY, FIO TEXT NOT NULL,  inn INT NOT NULL, number TEXT NOT NULL, pasport TEXT NOT NULL )''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
