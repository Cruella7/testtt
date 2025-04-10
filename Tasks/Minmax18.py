"""
Minmax18. Дано целое число N и набор из N целых чисел. Найти
количество элементов, содержащихся между первым и последним максимальным 
элементом. Если в наборе имеется единственный максимальный элемент, то 
вывести 0.
Гаврюшкин Максим
11.11.2023
Время: 7 min
"""
def podschet_elementov_v_intervale(spisok):
    znachenie_maksimuma = max(spisok)
    indeksy_maksimuma = [i for i, x in enumerate(spisok) if x == znachenie_maksimuma]

    if len(indeksy_maksimuma) == 1:
        return 0
    else:
        return indeksy_maksimuma[-1] - indeksy_maksimuma[0] - 1


chisla = [int(x) for x in input("Vvedite chisla cherez probel: ").split()]

rezultat = podschet_elementov_v_intervale(chisla)

print(rezultat)
