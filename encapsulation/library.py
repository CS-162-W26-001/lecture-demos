class Book:
    title: str
    author: str
    publication_year: int

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

def add(x:int, y:int) -> int:
    return x + y

def main() -> None:
    book = Book()
    book.title = "1984"
    book.author = "George Orwell"
    book.publication_year = 1949

    library = Library()
    # library.print()
    library.add_book(book)
    book.title = "Pride and Prejudice"
    library.print()
    # library.checkout(book)
    # library.print()

if __name__ == "__main__":
    main()
