"""Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена 
между точками A и B. Найти произведение длин отрезков AC и BC.
Арутюнян С.К. 32ИС-21. Затрачено 7 минут"""

def otrezki():
    A = float(input("Введите точку A: "))
    B = float(input("Введите точку B: "))
    C = float(input("Введите точку C (между A и B): "))

    AC = abs(C - A)
    BC = abs(B - C)

    product = AC * BC
    return product

result = otrezki()
print("Произведение длин отрезков AC и BC:", result)
