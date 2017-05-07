import os
import click

from .logic import random_quote, random_book

CONFIG_FILE = os.path.expanduser('~') + '/.goodquotes'


@click.command()
@click.option('--book', '-b', default=None, help='Title of the book')
@click.option('--library', '-l', default=None, help='Path to imported Goodreads library')
def cli(book, library):
    """ Generates a quote at random from your library.
    Given a book, it prints the quote specific to this book.
    """
    if library is not None and book is not None:
        click.echo('It seems that you are trying to perform two operations at the same time. But do not worry, we have got you covered, as always.')
        click.echo("We will import your library while you enjoy a memorable moment from '{}'.")

    if library is not None:
        import_library(library)

    if book is not None:
        quote_book(book)

    if book is None and library is None:
        quote_book(None)


def quote_book(book_title):
    if book_title:
        rquote = random_quote(book_title)
        click.echo(rquote)

    elif os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            KINDLE_LIBRARY = (config_file.readline().split('=')[1]).strip()

        selected_title, selected_author = random_book(KINDLE_LIBRARY)
        rquote = random_quote(selected_title, selected_author)
        click.echo(rquote)

    else:
        click.echo("You have to either import your Goodreads Library or tell me about your favourite novel! I will listen intently. :)")


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
