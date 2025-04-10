"""
String18. Дана строка. Преобразовать в ней все строчные буквы (как
латинские, так и русские) в прописные, а прописные — в строчные.
Гаврюшкин Максим
11.11.2023
Время: 5 min
"""
def invert(input_string):
    result_string = ""
    for char in input_string:
        if char.islower():
            result_string += char.upper()
        elif char.isupper():
            result_string += char.lower()
        else:
            result_string += char
    return result_string


input_str = input("Введите строку: ")
transformed_str = invert(input_str)
print(transformed_str)
