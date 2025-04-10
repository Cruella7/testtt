"""
Series18. Дано целое число N и набор из N целых чисел, упорядоченный
по возрастанию. Данный набор может содержать одинаковые элементы. 
Вывести в том же порядке все различные элементы данного набора.
Гаврюшкин Максим
11.11.2023
Время: 10 min
"""
def unique_elements_in_order(N, numbers):
    unique_elements = []

    for num in numbers:
        if num not in unique_elements:
            unique_elements.append(num)

    return unique_elements


try:
    N = int(input("N: "))

    numbers = [int(input(f"Введите число #{i + 1}: ")) for i in range(N)]
    ordered_unique_elements = unique_elements_in_order(N, numbers)

    print("Различные элементы в порядке возрастания:")
    for element in ordered_unique_elements:
        print(element)
except ValueError as ve:
    print(f"Ошибка: {ve}")
