class Reader:
    """
    Класс о данных клиента.
    """
    def __init__(self, reader_id: int, famil: str, name: str, otch: str, ticket: int):
        """
        Атрибуты класса:

        Код читателя
        Фамилия
        Имя
        Отчество
        № читательского билета
        """
        self.reader_id = reader_id
        self.famil = famil
        self.name = name
        self.otch = otch
        self.ticket = ticket
    def __str__(self):
        """
        Метод для получения информации о итателе в строковом формате
        """
        return f"{self.reader_id}. {self.famil} {self.name} {self.otch}  {self.ticket}"
