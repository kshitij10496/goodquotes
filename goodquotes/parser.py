import requests
from bs4 import BeautifulSoup

from .quote import Quote

# 1. Handle search operation
# 2. Create a soup from the response and send it to the parser
def search_quotes(book_title):
    ''' Searches for the top quotes of a book as on Goodreads.

    Parameters
    ==========
    book_title : str
        The title of the book we are interested in.

    Returns
    =======
    list of Quote objects
    '''
    base_url = 'https://www.goodreads.com/quotes/search'
    params = {'q': book_title}
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_quotes = []

    for quote in soup.findAll('div', 'quoteDetails '):
        # Extract the quote content div
        quote_content = quote.find('div', 'quoteText')
        stripped_quote = quote_content.text.split('//<![CDATA')[0]
        raw_quote = stripped_quote.split('\n')
        if len(raw_quote) != 9:
            continue

        quote_text, quote_author, quote_book_title = raw_quote[1].strip(), raw_quote[3].strip(), raw_quote[5].strip()

        tags_data = quote.find('div', 'greyText smallText left')
        # Check if tags are present for the quote
        if tags_data is not None and tags_data.text.split()[0] == 'tags:':
            quote_tags = tags_data.text.split()[1:]
        else:
            quote_tags = None

        new_quote = Quote(quote_text, quote_book_title, quote_author, tags=quote_tags)
        all_quotes.append(new_quote)

    return all_quotes
