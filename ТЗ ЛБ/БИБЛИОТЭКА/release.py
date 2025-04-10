class Release:
    """
    Класс о данных заказа
    """
    def __init__(self, reader_id: int, book_id: int, release_data: str):
        """
        Атрибуты класса:

       Код читателя
       Код книги
       Дата выдачи
        """
        self.reader_id = reader_id
        self.book_id = book_id
        self.release_data = release_data
    def __str__(self):
        """
        Метод для получения информации о выдачи книги в строковом формате
        """
        return f"{self.reader_id}. {self.book_id} {self.release_data}"
if __name__ == '__main__':
    releases = []
    """
    Чтение данных из файла и создание объектов Order
    """
    with open("release.txt", "r", encoding="ansi") as release_f:
        for line in release_f:
            release_id, book_id, reader_id, release_data = line.split(";")
            book_id = int(book_id)
            reader_id = int(reader_id)
            release_data = str(release_data)
            release = Release(release_id, book_id, reader_id, release_data)
            releases.append(release)
    """
    Запись отсортированных данных в файл
    """
    with open("release_f_sorted.txt", "w", encoding="utf-8") as release_f_sorted_f:
        release_f_sorted_f.write("release_id, book_id, reader_id, release_data\n")
        for release in sorted(release, key=lambda x: x.release_data, reverse=True):
            release_f_sorted_f.write(str(release)+"\n")
print("release done")
