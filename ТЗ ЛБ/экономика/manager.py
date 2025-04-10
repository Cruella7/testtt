class Manager:
    """
    Класс о данных менеджера
    """
    def __init__(self, manager_id: int, name: str, city: str, comm: float):
        """
        Атрибуты класса:

        идентификатор менеджера
        имя
        город
        комиссия менеджера
        """
        self.manager_id = manager_id
        self.name = name
        self.city = city
        self.comm = comm
    def __str__(self):
        """
        Метод для получения информации о менеджере в строковом формате
        """
        return f"{self.manager_id}. {self.name} {self.city} {self.comm}"
