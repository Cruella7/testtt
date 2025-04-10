"""
For18. Дано вещественное число A и целое число N (> 0).
Используя один цикл, найти значение выражения
1 - A + A**2 - A**3 + ... + (−1)**N*A**N.
Гаврюшкин Максим
11.11.2023
Время: 4 min
"""
def vychislit_vyrazhenie(X, Y):
    rezultat = 0
    znak = 1

    for i in range(Y + 1):
        rezultat += znak * X ** i
        znak *= -1

    return rezultat

# Пример использования
V = float(input("V: "))
N = int(input("N (> 0): "))

if N > 0:
    rez = vychislit_vyrazhenie(V, N)
    print(f"Значение: {rez}")
else:
    print("Не правильно")
