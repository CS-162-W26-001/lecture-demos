from enum import Enum

IN_STOCK = "in stock"
CHECKED_OUT = "checked out"
ON_HOLD = "on hold"
PAST_DUE = "past due"

class BookStatus(Enum):
    IN_STOCK = 1
    CHECKED_OUT = 2
    ON_HOLD = 3
    PAST_DUE = 4

class Category(Enum):
    FICTION = 1
    NON_FICTION = 2
    CHILDRENS = 3
    NEWS = 4
    TECHNICAL = 5

class Book:
    title: str
    author: str
    publication_year: int
    status: BookStatus
    category: Category | None

class Library:
    _books: list[Book]
    _checked_out_books: list[Book]

    def __init__(self) -> None:
        self._books = []
        self._checked_out_books = []

    def checkout(self, book: Book) -> None:
        self._books.remove(book)
        self._checked_out_books.append(book)

    def add_book(self, book: Book) -> None:
        copy = self._copy_book(book)
        self._books.append(copy)
    
    def print(self) -> None:
        print("Available books:")
        for book in self._books:
            print(book.title)
        
        print("Checked out books:")
        for book in self._checked_out_books:
            print(book.title)

    def get_checked_out_books(self) -> list[Book]:
        books_copy = []
        for book in self._checked_out_books:
            books_copy.append(book)
        return books_copy
    
    def set_checked_out_books(self, books: list[Book]) -> None:
        self._checked_out_books = books

    def _copy_book(self, book: Book) -> Book:
        book_copy = Book()
        book_copy.title = book.title
        book_copy.author = book.author
        book_copy.publication_year = book.publication_year
        return book_copy
    
    def find_book_by_title(self, title: str) -> Book | None:
        for book in self._books:
            if book.title == title:
                return book
        return None

def add(x:int, y:int) -> int:
    return x + y

def main() -> None:
    book = Book()
    book.title = "1984"
    book.author = "George Orwell"
    book.publication_year = 1949

    book2 = Book()
    book2.title = "Hungry Caterpiller"
    book2.author = "Eric Carle"
    book2.publication_year = 1969

    book3 = Book()
    book3.title = "Do Androids Dream of Electric Sheep"
    book3.author = "Philip K. Dick"
    book3.publication_year = 1968

    book4 = None
    # title = input("Enter a title:")
    # if title:
    #     book4 = Book()
    #     book4.title = title

    library = Library()
    # library.print()
    library.add_book(book)
    library.add_book(book2)
    library.add_book(book3)
    # library.print()
    # library.checkout(book)
    # library.print()

    book_by_title = library.find_book_by_title("1984")
    if book_by_title is not None:
        book_by_title.status = BookStatus("pizza")
        print(f"{book_by_title.title}, {book_by_title.status}")

if __name__ == "__main__":
    main()
