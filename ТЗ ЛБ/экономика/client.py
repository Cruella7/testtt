class Client:
    """
    Класс о данных клиента.
    """
    def __init__(self, client_id: int, name: str, city: str, rating: int, manager_id: int):
        """
        Атрибуты класса:

        идентификатор клиента
        имя
        город
        рейтинг
        идентификатор менеджера клиента
        """
        self.client_id = client_id
        self.name = name
        self.city = city
        self.rating = rating
        self.manager_id = manager_id
    def __str__(self):
        """
        Метод для получения информации о клиенте в строковом формате
        """
        return f"{self.client_id}. {self.name} {self.city} {self.rating} {self.manager_id}"
