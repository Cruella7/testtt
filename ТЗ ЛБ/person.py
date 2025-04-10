libr = ['Репка', 'Морозко', 'Колобок']
books = [Book() for i in range(3)]
for i in range(len(titles)):
    books[i].set_libr(libr[i])

sorted_books = sorted(books, key=lambda x: x.title)
for b in sorted_books:
    print(b.libr)