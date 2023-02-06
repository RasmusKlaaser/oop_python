
class Book():
    def __init__(self, title: str, author: str, price: float, rating: float):
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        return self.title

class Store():
    def __init__(self, name: str, rating: float):
        self.__name = name
        self.__rating = rating
        self.books = []

    def can_add_book(self, book: Book):
        if book.rating >= self.__rating:
            if len(self.books) > 0:
                for storeBook in self.books:
                    if storeBook.title == book.title and storeBook.author == book.author:
                        return False
                    else:
                        return True
            else:
                return True
        else:
            return False


    def add_book(self, book: Book):
       if self.can_add_book(book):
           self.books.append(book)


    def can_remove_book(self, book: Book):
        if book.rating <= self.__rating:
            if len(self.books) < 0:
                for storeBook in self.books:
                    if storeBook.title == book.title and storeBook.author == book.author:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return True
    def get_all_books(self):
        return self.books


    def remove_book(self, book: Book):
        if self.can_remove_book(book):
            self.books.remove(book)


    def get_books_by_price(self):
        return sorted(self.books, key=lambda book: book.price)



    def get_most_popular_book(self):
        sorted_books = sorted(self.books, key=lambda book: book.rating)
        highest_books = []
        for book in self.books:
            if book.rating == sorted_books[-1].rating:
                highest_books.append(book)
        return highest_books

book1 = Book("Läänerindel muutuseta", "Remarque", 25.99, 10.6)
book2 = Book("Läänerindel muutuseta 2", "Remarque", 20.99, 19.6)
book3 = Book("Läänerindel muutuseta 3", "Remarque", 22.99, 15.6)
print(book1)
store = Store("TÜ raamatupood", 8.0)
print(store.can_add_book(book1))
store.add_book(book1)
store.add_book(book2)
store.add_book(book3)
store.get_books_by_price()


