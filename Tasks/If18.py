"""
If18. Даны три целых числа, одно из которых отлично от двух других,
равных между собой. Определить порядковый номер числа, отличного от 
остальных.
Гаврюшкин Максим
11.11.2023
Время: 3 min
"""
def opredelitel(a, b, c):
    if a == b:
        return 3
    elif a == c:
        return 2
    else:
        return 1

n1 = int(input("1: "))
n2 = int(input("2: "))
n3 = int(input("3: "))

result = opredelitel(n1, n2, n3)
print(result)
