import os
import click

CONFIG_FILE = os.path.expanduser('~') + './goodquotes'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--book', default=None, type=unicode)
def quote(book):
    if book:
        rquote = random_quote(book)
        click.echo(rquote)

    elif os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            KINDLE_LIBRARY = config_file.readline()

        selected_book = random_book(KINDLE_LIBRARY)
        rquote = random_quote(selected_book)
        click.echo(rquote)

    else:
        click.echo("Either import your Kindle Library or tell me about your favourite novel ! :)")

@cli.command('import')
@click.argument(filepath)
def import_library(filepath):
    if os.path.isfile(filepath):
        _, file_ext = os.path.splitext(filepath)
        if file_ext == '.csv':
            KINDLE_LIBRARY = os.path.abspath(filepath)
            with open(CONFIG_FILE, 'w') as config_file:
                config_file.write('KINDLE_LIBRARY = {}'.format(KINDLE_LIBRARY))
            # store the path in app config
            
        else
    else:
        click.echo('It seems that you have entered an incorrect file.')
        click.echo('Enter a valid csv file imported from Goodreads.')
