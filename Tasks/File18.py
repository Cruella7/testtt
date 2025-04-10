"""
File18. Дан файл вещественных чисел. Найти его первый локальный
минимум (локальным минимумом называется элемент, который меньше своих 
соседей).
Гаврюшкин Максим
11.11.2023
Время: 5 min
"""
def najti_localnyi_minimum(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    chisla = [float(number) for line in lines for number in line.strip().split()]

    for i in range(1, len(chisla) - 1):
        if chisla[i - 1] > chisla[i] < chisla[i + 1]:
            return chisla[i]

    return None

# Пример использования
put_k_failu = 'цифры.txt'  # Замените 'vash_fail.txt' на путь к вашему файлу
rezultat = najti_localnyi_minimum(put_k_failu)

if rezultat is not None:
    print(f"Локальный минимум: {rezultat}")
else:
    print("Локальный минимум пропал.")

