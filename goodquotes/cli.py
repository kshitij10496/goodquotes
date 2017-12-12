import os
import click

from .logic import random_quote, random_book

CONFIG_FILE = os.path.expanduser('~') + '/.goodquotes'

@click.command()
@click.option('--book', '-b', default=None, help='Title of the book')
@click.option('--author', '-a', default=None, help='Name of the author')
@click.option('--library', '-l', default=None, help='Path to the Goodreads library')
def cli(book, author, library):
    """ Generates a quote at random from your library.

    Given a book, it prints the quote from this book.
    Given the name of an author, the application prints a quote from among their books.
    """
    #print("Book:", book)
    #print("Author:", author)
    #print("Library:", library)

    if library is not None:
        import_library(library)
        return

    lib_exists = is_lib()
    
    if book is not None:
        quote_book(book)
    elif author is not None:
        quote_author(author)
    elif lib_exists:
        quote_library()
    else:
        click.echo(random_quote())


def quote_book(book_title):
    if book_title:
        rquote = random_quote(book_title)
        click.echo(rquote)

def is_lib():
    return os.path.exists(CONFIG_FILE)


def quote_library():
    with open(CONFIG_FILE, 'r') as config_file:
        KINDLE_LIBRARY = (config_file.readline().split('=')[1]).strip()

    selected_title, selected_author = random_book(KINDLE_LIBRARY)
    rquote = random_quote(selected_title, selected_author)
    click.echo(rquote)


def import_library(filepath):
    if os.path.isfile(filepath):
        _, file_ext = os.path.splitext(filepath)
        if file_ext == '.csv':
            KINDLE_LIBRARY = os.path.abspath(filepath)
            with open(CONFIG_FILE, 'w+') as config_file:
                config_file.write('KINDLE_LIBRARY={}'.format(KINDLE_LIBRARY))
            # store the path in app config
            click.echo('Successfully imported your library. :)\nExecute "goodquotes" to relive moments from these books.')
        else:
            click.echo('We are having trouble importing your library. It seems that you have entered an incorrect file.')
            click.echo('Enter a valid csv file imported from Goodreads.')

    else:
        click.echo('The path to the file does not exist. Kindly check the entered file path.')
