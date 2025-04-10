from decimal import Decimal
#Округление
num1 = Decimal(input('Введите первое число:'))
num2 = Decimal(input('Введите второе число:'))
print("Первое число:", num1)
print("Второе число:", num2)
num3 = num1 / num2
print("Первое число разделенное на второе число:", num3)
num4 = round(num3, 2)
print("Округленное число:", num4)


#Сравнение
a = Decimal(input('Введите первое число:'))
b = Decimal(input('Введите второе число:'))
c = Decimal(input('Введите третье число:'))
d = a + b
print("a:", a)
print("b:", b)
print("c:", c)
print("a+b:", d)
print("a+b==c?:", c == d)
