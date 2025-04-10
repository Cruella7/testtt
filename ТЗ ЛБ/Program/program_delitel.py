"""
Разработать программу для нахождения наибольшего общего делителя
"""
def delitel(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))

result = delitel(n1, n2)
print("Наибольший общий делитель:", result)
