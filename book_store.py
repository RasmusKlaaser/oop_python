class Book():
    def __init__(self, title: str, author: str, price: float, rating: float):
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store():
    books = []

    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating

    def can_add_book(self, book: Book):
        result = False
        if len(self.books) > 0:
            for storeBook in self.books:
                if storeBook.title == book.title and storeBook.author == book.author and storeBook.price == book.price:
                    result = False
                else:
                    if book.rating >= self.rating:
                        result = True
        else:
            if book.rating >= self.rating:
                result = True
        return result


book1 = Book("Läänerindel muutuseta", "Remarque", 20.99, 10.6)
print(book1)
store = Store("TÜ raamatupood", 8.0)
print(store.can_add_book(book1))


