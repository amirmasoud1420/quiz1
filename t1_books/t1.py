import dill


class Book:
    pass


with open('books.dill', 'rb') as f:
    book_list = dill.load(f)

ISBN_list = sorted(book_list, key=lambda x: x.ISBN)
name_list = sorted(book_list, key=lambda x: x.name)
publish_list = sorted(book_list, key=lambda x: x.publish_date)
author_filter = filter(lambda x: x.author == 'George Orwell', book_list)
author_filter = filter(lambda x: x.publisher == 'Akbar pub' or x.publisher == 'Asqar pub', book_list)
author_filter = filter(lambda x: x.publish_date >= 2001, book_list)
