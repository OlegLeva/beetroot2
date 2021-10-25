class Library:
    books = []
    authors = []

    def __init__(self, name):
        self.name = name

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        if book not in self.books:
            self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        Book.count += 1
        return book

    def group_by_author(self, author_name):
        for author in self.authors:
            if author.name == author_name:
                return f'Author: {author.name}\nBooks: {author.books}'
            else:
                return "There is no such author"

    def group_by_year(self, year_pablication):
        list_by_year = []
        for book in self.books:
            if book.year == year_pablication:
                list_by_year.append(book.name)
        return f'Books of {year_pablication}\n{list_by_year}'



class Book:
    count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'Book: {self.name}\nDate of publishing: {self.year}\nAuthor: {self.author.name}'

    def __str__(self):
        return f'Book: {self.name}\nDate of publishing: {self.year}\n{self.author.name}'


class Author:
    def __init__(self, name, country, birthday, *books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f'Author: {self.name}\nCountry birthday: {self.country}\nBirthday: {self.birthday}\n' \
               f'Books {self.books}'

    def __str__(self):
        return f'Author: {self.name}\nCountry birthday: {self.country}\nBirthday: {self.birthday}\n' \
               f'Books {self.books}'


laurent_gounelle = Author('Laurent Gounelle', 'France', '10.08.1966', ['Бог всегда путешествует инкогнито',
                                                                       'Человек который хотел быть счастливым',
                                                                       'Я обещаю тебе волю'])
geri_bishop = Author('Geri Bishop', 'Scotland', '22.01.1979', ['Stop doing that sh*t',
                                                               'Unfu*k yourself',
                                                               'Разгреби своё гавно'])
modern = Library('Modern')
got_travels = modern.new_book('Бог всегда путешествует инкогнито', 2010, laurent_gounelle)
the_man_who_wanted = modern.new_book('Человек который хотел быть счастливым', 2008, laurent_gounelle)
unfuck_yourself = modern.new_book('Unfu*k yourself', 2010, geri_bishop)
# print(got_travels.year)
print(got_travels)
print()
# print(Library.authors)
print(Book.count)
print(len(Library.books))
print(len(Library.authors))
print(modern.group_by_author('Laurent Gounelle'))
print()
print(modern.group_by_year(2010))
# print(Library.books)

