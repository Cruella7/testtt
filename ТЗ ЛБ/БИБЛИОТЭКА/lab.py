from book import Book
from reader import Reader
from release import Release
from datetime import datetime

class Lab:
    def __init__(self, lab_id: int):
        self.lab_id = lab_id
        self.books = []
        self.readers = []
        self.releases = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_client(self, reader: Reader):
        self.readers.append(reader)

    def add_order(self, release: Release):
        self.releases.append(release)

    def __str__(self):
        return str(self.lab_id)

    def read_books(self, books_fname):
        with open(books_fname, "r", encoding='UTF8') as books_f:
            for line in books_f:
                book_id, name, author, janr, god = line.split(";")
                book_id = int(book_id)
                god = int(god)
                book = Book(book_id, name, author, janr, god)
                self.books.append(book)

    def read_readers(self, readers_fname):
        with open(readers_fname, "r", encoding='UTF8') as readers_f:
            for line in readers_f:
                reader_id, famil, name, otch, ticket = line.split(";")
                reader_id = int(reader_id)
                ticket = int(ticket)
                reader = Reader(reader_id, famil, name, otch, ticket)
                self.readers.append(reader)

    def read_release(self, release_fname):
        with open(release_fname, "r", encoding='UTF8') as release_f:
            for line in release_f:
                reader_id, book_id, release_data = line.strip().split(";")
                reader_id = int(reader_id)
                book_id = int(book_id)
                release = Release(reader_id, book_id, release_data)
                self.releases.append(release)

    def release_b_data(self):
        # Отсортируйте данные по дате с использованием datetime
        sorted_releases = sorted(self.releases, key=lambda x: datetime.strptime(x.release_data, "%Y-%m-%d"))

        # Откройте файл для записи
        with open('release_sorted.txt', 'w', encoding='UTF8') as f:
            for release in sorted_releases:
                f.write(f"{release.reader_id};{release.book_id};{release.release_data}\n")

if __name__ == '__main__':
    lab = Lab(1)
    lab.read_books("books.txt")
    lab.read_readers("readers.txt")
    lab.read_release("release.txt")
    lab.release_b_data()

