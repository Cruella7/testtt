import sqlite3
# Создаем подключение к базе данных
connection = sqlite3.connect("mydatabase.db")
# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()

# Вставляем данные в таблицу "Game"
cursor.execute("INSERT INTO Game (name, price, person, reiting) VALUES (?, ?, ?, ?)", ("Барби", "20.000",  "2", "4"))

# Вставляем данные в таблицу "Developer"
cursor.execute("INSERT INTO Developer (country, company, emaill, price, inn, number) VALUES (?, ?, ?, ?, ?,?)", ("Россия", "GamesSseS", "gamesesss@mail.ru", "20.000", "325891254378", "89162160712"))

# Вставляем данные в таблицу "Development_tools"
cursor.execute("INSERT INTO Development_tools(language, datebase, engine ) VALUES (?, ?, ?)", ("Python", "SQL" ,"Пакет PyGame"))

# Вставляем данные в таблицу "Post"
cursor.execute("INSERT INTO Post (salaru, grafic, name, responsibilities) VALUES (?, ?, ?, ?)", ( "100.000", "5/2", "Программист", "Разработка программных модудей"))
cursor.execute("INSERT INTO Post (salaru, grafic, name, responsibilities) VALUES (?, ?, ?,?)", ("70.000", "5/2", "Менеджер", "Поиск клиентов и продажи"))

# Вставляем данные в таблицу "Worker"
cursor.execute("INSERT INTO Worker (FIO, inn, number, pasport) VALUES (?, ?, ?, ?)", ( "Фридман Эдвард Каренович", "125898754323", "89224370912", "452222 546476"))
cursor.execute("INSERT INTO Worker (FIO, inn, number, pasport) VALUES (?, ?, ?, ?)", ( "Иванько Сергей Антонович", "348798234365", "89254330972", "452065 766476"))

# Сохраняем изменения и закрываем соединениеconnection.commit()
connection.close()
