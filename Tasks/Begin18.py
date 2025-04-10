"""
Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена
между точками A и B. Найти произведение длин отрезков AC и BC.
Гаврюшкин Максим
11.11.2023
Время: 4 min
"""
def a(A, B, C):
    AC = abs(C - A)
    BC = abs(B - C)
    p = AC * BC
    return p


A = 2
B = 2
C = 8

res = a(A, B, C)
print(res)
