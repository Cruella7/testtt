from tkinter import *

# функция для вычисления результата
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = entry3.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = "Неверная операция"

    label_result.config(text="Результат: " + str(result))

# создание окна
root = Tk()
root.title("Калькулятор")

# создание интерфейса
label1 = Label(root, text="Первое число:")
label2 = Label(root, text="Второе число:")
label3 = Label(root, text="Что будем делать?(+, -, *, /):")
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
button_calc = Button(root, text="Вычислить", command=calculate)
label_result = Label(root, text="Результат:")

# размещение элементов на окне
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)
button_calc.grid(row=3, column=0, columnspan=2)
label_result.grid(row=4, column=0, columnspan=2)

# запуск основного цикла программы
root.mainloop()