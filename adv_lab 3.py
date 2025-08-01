class Book:
    total_books = 0

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.total_books += 1

    def update_title(self, new_title):
        self.title = new_title

    def update_author(self, new_author):
        self.author = new_author

    def display_info(self, user_type="reader"):
        if user_type == "librarian":
            print(f"[LIBRARIAN] Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
        else:
            print(f"[READER] Title: {self.title}, Author: {self.author}")

    @staticmethod
    def book_info():
        print("Books contain title, author, and ISBN.")

    @classmethod
    def get_total_books(cls):
        return cls.total_books


class Author:
    total_authors = 0

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.books = []
        Author.total_authors += 1

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]

    @staticmethod
    def author_info():
        print("Authors have names, birthdates, and books they've written.")

    @classmethod
    def get_total_authors(cls):
        return cls.total_authors


class Library:
    library_count = 0

    def __init__(self):
        self.books = []
        self.authors = []
        Library.library_count += 1

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

    @staticmethod
    def library_info():
        print("Libraries store books and authors.")

    @classmethod
    def get_library_count(cls):
        return cls.library_count

a1 = Author("J.K. Rowling", "1965-07-31")
b1 = Book("Harry Potter", "J.K. Rowling", "1234")
a1.add_book(b1)

lib = Library()
lib.add_book(b1)
lib.list_books()

b1.display_info("librarian")

print(Book.get_total_books())
print(Author.get_total_authors())
print(Library.get_library_count())
