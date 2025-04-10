"""
Recur17. Вывести значение целочисленного выражения,
заданного в виде строки S. Выражение определяется следующим образом:
	<выражение>	::=	<цифра> |
		(<выражение><знак><выражение>)
	<знак>	::=	+ | − | *
Гаврюшкин Максим
11.11.2023
Время: 25 min
"""
import ast

def vychislit_znachenie_vyrazheniya(s):
    try:
        tree = ast.parse(s, mode='eval')
        result = eval(compile(tree, filename='<string>', mode='eval'))
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

vyrazhenie = "(1+2)*16"
rezultat = vychislit_znachenie_vyrazheniya(vyrazhenie)

if rezultat is not None:
    print(f"Результат выражения: {rezultat}")
