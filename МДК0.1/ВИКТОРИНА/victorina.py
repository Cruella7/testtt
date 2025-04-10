from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина - шуточные вопросы")
root.geometry("600x600")

def que_one():
    question = Label(root, text="В каком названии города заключено одно мужское имя и сто женских?")
    answer = Entry()
    btn = Button(root, text="Ответить", command=lambda: game1(que_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(que_two):
        if answer.get() == "Севастополь":
            que_two()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз")


def que_two():
    question_2 = Label(root, text="У семерых братьев по сестре. Сколько всего сестер?")
    answer_2 = Entry()
    btn_2 = Button(root, text="Ответить", command=lambda: game2(que_three))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game2(que_three):
        if answer_2.get() == "Одна":
            que_three()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз")

def que_three():
    question_3 = Label(root, text="Из какой посуды не едят?")
    answer_3 = Entry()
    btn_3 = Button(root, text="Ответить", command=lambda: game3(que_four))
    question_3.grid()
    answer_3.grid()
    btn_3.grid()

    def game3(que_four):
        if answer_3.get() == "Пустой":
            que_four()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз")


def que_four():
    question_4 = Label(root, text="Как написать «сухая трава» четырьмя буквами?")
    answer_4 = Entry()
    btn_4 = Button(root, text="Ответить",  command=lambda: game4(que_five))
    question_4.grid()
    answer_4.grid()
    btn_4.grid()

    def game4(que_five):
        if answer_4.get() == "Сено":
            que_five()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз")


def que_five():
    question_5 = Label(root, text="Что многие готовят, но никогда не едят?")
    answer_5 = Entry()
    btn_5 = Button(root, text="Ответить!",  command=lambda: game5(que_five))
    question_5.grid()
    answer_5.grid()
    btn_5.grid()

    def game5(que_five):
        if answer_5.get() == "Уроки":
            messagebox.showinfo("Победа!")
            que_five()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз")

que_one()
root.mainloop()
