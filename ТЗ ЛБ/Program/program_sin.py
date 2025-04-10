"""
Вычислить значение sin(x) с точностью до epsilon при помощи разложения в ряд
Построить блок-схему
"""
def sin(x, epsilon):
    result = 0
    n = x
    i = 1
    while abs(n) > epsilon:
        result += n
        n = (-1) * n * x * x / ((2 * i + 1) * (2 * i))
        i += 1
    return result

x = float(input("Введите значение x для вычисления синуса: "))
epsilon = float(input("Введите значение epsilon: "))

result = sin(x, epsilon)
print("Значение sin(x) с точностью до epsilon:", result)
