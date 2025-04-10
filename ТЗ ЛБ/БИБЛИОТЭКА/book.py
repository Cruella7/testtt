class Book:
    """
    Класс информации о книгах
    """
    def __init__(self, book_id: int, name: str, author: str, janr: str, god: int):
        """
        Атрибуты класса:

        Код книги
        Название
        Автор
        Жанр
        Год издания
        """
        self.book_id = book_id
        self.name = name
        self.author = author
        self.janr = janr
        self.god = god
    def __str__(self):
        """
        Метод для получения информации о книге в строковом формате
        """
        return f"{self. book_id}. {self.name} {self.author} {self.janr} {self.god}"
