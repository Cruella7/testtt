"""
Text18. Дано целое число K и текстовый файл. Удалить из каждой строки
файла первые K символов (если длина строки меньше K, то удалить из нее 
все символы).
Гаврюшкин Максим
11.11.2023
Время: 7 min
"""
def file(file_path, k_value):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        with open(file_path, 'w') as f:
            for line in lines:
                new_line = line[k_value:] if len(line) >= k_value else ''
                f.write(new_line)

        print(f"Успешно удалены первые {k_value} символов из каждой строки файла.")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

try:
    file_path = input("Введите имя файла: ")
    k_value = int(input("Введите количество символов для удаления: "))
    file(file_path, k_value)
except ValueError:
    print("Некорректный ввод числа.")
