"""Array18. Дан массив A ненулевых целых чисел размера 10. Вывести 
значение первого из тех его элементов AK, которые удовлетворяют 
неравенству AK < A10. Если таких элементов нет, то вывести 0.
Арутюнян С.К. 32ИС-21. Затрачено 10 минут"""

def ak (A):
    for AK in A[:9]:
        if AK < A[9]:
            return AK
    return 0


A = [2, 3, 7, 19, 10, 15, 12, 17, 19, 20]
result = ak(A)

print("Результат:", result)

