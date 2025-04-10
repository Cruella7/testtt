"""
Программа на поиск максимального и минимального числа из словаря
"""
num = []
while True:
    ss = input('Ожидается ввод первого числа:')
    if ss is not None:
        num.append(ss)

    sss = input('Ожидается ввод второго числа:')
    if sss is not None:
        num.append(sss)
        break
if num:
    if len(num) == 1:
        print('Вы ввели одну цифру: ', num[0])
    else:
        print('\nВыберите действие:')
        print('   выбрать минимальное число;')
        print('   выбрать максимальное число\n')
        rez = None
        while True:
            ss = input('Введите 1 или 2:')
            ss = ss.strip()
            if ss == '1':
                rez = min(num)
                print('Минимальное число:', rez)
            elif ss == '2':
                rez = max(num)
                print('Максимальное число:', rez)
            else:
                print('Неправильное действие.\n')
            if rez is not None:
                break
else:
    print('Вы ничего не ввели.')