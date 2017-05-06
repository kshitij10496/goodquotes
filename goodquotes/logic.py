import random
import csv

from .parser import search_quotes

def random_book(file):
    book_title, book_author = None, None
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        num_of_books = len(data) - 1

        selected_book_id = random.randint(1, num_of_books)
        selected_book = data[selected_book_id]
        book_title, book_author = selected_book[1], selected_book[2]

    return book_title, book_author

def random_quote(book_title, book_author=None):
    book_quotes = search_quotes(book_title)
    random_quote = random.choice(book_quotes)
    return random_quote
