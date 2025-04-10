"""
@@ обозначает ошибку
!! обозначает предупреждение
// обозначает информационное сообщение
** обозначает подробное сообщение
Напишите программу, которая принимает строки до точки и выводит,
какого типа это сообщение. Если сообщение не содержит модификаторов,
проигнорируйте его.

Sample Input:
!! cannot resolve this method !!
@@ invalid type @@
// here I change the variables name //
** this class is used for operating with the database, including CRUD operations and registering new users **
"""

def invalid_type():
    print('@@ invalid type @@')

def cannot_resolve_this_method():
    print('!! cannot resolve this method !!')

def here_I_change_the_variables_name():
    print('// here I change the variables name //')

def  this_class_is_used():
    print('** this class is used for operating with the database, including CRUD operations and registering new users **')

def main():
    while True:
        print("Меню:")
        print("1. @@ - обозначает ошибк")
        print("2. !! - обозначает предупреждение")
        print("3. // - обозначает информационное сообщение")
        print("4. ** - обозначает подробное сообщение")
        print("4. Выход")

        tip = input("Выберите тип данных (1-4) или введите 5 для выхода: ")
        if tip == "1":
            invalid_type()
        elif tip == "2":
            cannot_resolve_this_method()
        elif tip == "3":
            here_I_change_the_variables_name()
        elif tip == "4":
            this_class_is_used()
        elif tip == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
main()
