import dill

with open('books.dill', 'rb') as f:
    book_list = dill.load(f)

ISBN = sorted(book_list,lambda x :book_list[1].ISBN)
