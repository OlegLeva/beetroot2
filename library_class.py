class Library:
    books = []
    authors = []

    def __init__(self, name):
        self.name = name

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author)
        return book


class Book:
    count = len(Library.books)

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author


class Author:
    def __init__(self, name, country, birthday, *books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books


laurent_gounelle = Author('Laurent Gounelle', 'France', '10.08.1966', ['Бог всегда путешествует инкогнито',
                                                                       'Человек который хотел быть счастливым',
                                                                       'Я обещаю тебе волю'])
b = Library('Бог всегда путешествует инкогнито')
b.new_book('Бог всегда путешествует инкогнито', 2010, laurent_gounelle)
print(b.name)
print(Library.books[0])
print(Library.authors)
print(Book.count)
print(len(Library.books))
