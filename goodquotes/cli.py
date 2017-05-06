import os
import click

from .logic import random_quote, random_book

CONFIG_FILE = os.path.expanduser('~') + '/.goodquotes'

@click.group()
def cli():
    pass

@cli.command('book')
@click.argument('book', nargs=-1)
def quote_book(book):
    book_title = ' '.join(book)
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

@cli.command('import')
@click.argument('filepath')
def import_library(filepath):
    if os.path.isfile(filepath):
        _, file_ext = os.path.splitext(filepath)
        if file_ext == '.csv':
            KINDLE_LIBRARY = os.path.abspath(filepath)
            with open(CONFIG_FILE, 'w+') as config_file:
                config_file.write('KINDLE_LIBRARY={}'.format(KINDLE_LIBRARY))
            # store the path in app config
        else:
            click.echo('It seems that you have entered an incorrect file.')
            click.echo('Enter a valid csv file imported from Goodreads.')

    else:
        click.echo('It seems that you have entered an incorrect file.')
        click.echo('Enter a valid csv file imported from Goodreads.')
