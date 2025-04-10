import tkinter as tk
#класс root с кодами каждого цвета
root = tk.Tk()

def insert_color(color):
    color_code = {
        "красный": "#ff0000",
        "оранжевый": "#ff7d00",
        "желтый": "#ffff00",
        "зеленый": "#00ff00",
        "голубой": "#007dff",
        "синий": "#0000ff",
        "фиолетовый": "#7d00ff"
    }
    #при нажатии на одну из кнопок с цветами
    color_entry.delete(0, tk.END)
    color_entry.insert(0, color_code[color])


#создает кнопку с текстом названия цвета и кодом цвета
#Кнопка при нажатии вызывает функцию insert_color() с аргументом названия цвета.
r_but = tk.Button(root, text="Красный", bg="#ff0000", command=lambda: insert_color("красный"))

or_but = tk.Button(root, text="Оранжевый", bg="#ff7d00", command=lambda: insert_color("оранжевый"))

yel_but = tk.Button(root, text="Желтый", bg="#ffff00", command=lambda: insert_color("желтый"))

gr_but = tk.Button(root, text="Зеленый", bg="#00ff00", command=lambda: insert_color("зеленый"))

bl_but = tk.Button(root, text="Голубой", bg="#007dff", command=lambda: insert_color("голубой"))

in_but = tk.Button(root, text="Синий", bg="#0000ff", command=lambda: insert_color("синий"))

vio_but = tk.Button(root, text="Фиолетовый", bg="#7d00ff", command=lambda: insert_color("фиолетовый"))

color_label = tk.Label(root, text="") #для отображения
color_entry = tk.Entry(root) #для ввода кода цвета
#размещает виджеты друг за другом в порядке создания
r_but.pack()
or_but.pack()
yel_but.pack()
gr_but.pack()
bl_but.pack()
in_but.pack()
vio_but.pack()

color_entry.pack()

root.mainloop()