class Mode1Window:
    def __init__(self, title, x, y, width, height, color, visible=True, with_border=True):
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = visible
        self.with_border = with_border

    def horizontal(self, distance):
        self.x += distance

    def toggle_visibility(self):
        self.visible = not self.visible

    def toggle_border(self):
        self.with_border = not self.with_border

    def display_info(self):
        print(f"Заголовок: {self.title}")
        print(f"Позиция: ({self.x}, {self.y})")
        print(f"Размер: {self.width} x {self.height}")
        print(f"Цвет: {self.color}")
        print(f"Видимость: {'Видимо' if self.visible else 'Скрыто'}")
        print(f"Рамка: {'С рамкой' if self.with_border else 'Без рамки'}")

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
окно1 = Mode1Window("Моё домашнее задание", 200, 200, 400, 400, "Розовый")
окно1.display_info()

окно1.horizontal(70)
окно1.toggle_visibility()
окно1.toggle_border()

print("\nПосле операций:")
окно1.display_info()

# Создание списка окон
окна = [Mode1Window("Моё домашнее задание", 200, 200, 400, 400, "Розовый"),
        Mode1Window("Другое окно", 100, 100, 300, 300, "Синий")]

# Сортировка списка окон по площади
окна_отсортированные = sorted(окна, key=lambda x: x.area())

# Вывод отсортированных окон
for окно in окна_отсортированные:
    окно.display_info()
