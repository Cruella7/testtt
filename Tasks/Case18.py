"""
Case18. Дано целое число в диапазоне 100–999. Вывести
строку-описание данного числа, например: 256 — «двести пятьдесят шесть», 
814 — «восемьсот четырнадцать».
Гаврюшкин Максим
11.11.2023
Время: 18 min
"""
def number_name(num):
    if not (100 <= num <= 999):
        return "Не входит в диапозон"

    ed_dict = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    desyatkiex_dict = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    desyatki_dict = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
    sotnyi_dict = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}


    sotnyi, remainder = divmod(num, 100)
    desyatki, ed = divmod(remainder, 10)

    des = ""
    des += sotnyi_dict.get(sotnyi, '')

    case_desyatki = {
        0: '',
        1: f" {desyatkiex_dict.get(remainder, '')}",
        2: f" {desyatki_dict.get(desyatki, '')}",
        3: f" {desyatki_dict.get(desyatki, '')}",
        4: f" {desyatki_dict.get(desyatki, '')}",
        5: f" {desyatki_dict.get(desyatki, '')}",
        6: f" {desyatki_dict.get(desyatki, '')}",
        7: f" {desyatki_dict.get(desyatki, '')}",
        8: f" {desyatki_dict.get(desyatki, '')}",
        9: f" {desyatki_dict.get(desyatki, '')}",
    }

    des += case_desyatki[desyatki]

    case_ed = {
        0: '',
        1: f" {ed_dict.get(ed, '')}",
        2: f" {ed_dict.get(ed, '')}",
        3: f" {ed_dict.get(ed, '')}",
        4: f" {ed_dict.get(ed, '')}",
        5: f" {ed_dict.get(ed, '')}",
        6: f" {ed_dict.get(ed, '')}",
        7: f" {ed_dict.get(ed, '')}",
        8: f" {ed_dict.get(ed, '')}",
        9: f" {ed_dict.get(ed, '')}",
    }

    des += case_ed[ed]

    return des.strip()

number = int(input("Ввод"))
result = number_name(number)
print(result)
