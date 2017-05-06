import textwrap

class Quote(object):

    def __init__(self, quote_text, book_title, author, tags=[]):
        self.quote_text = quote_text
        self.book_title = book_title
        self.author = author
        self.tags = tags

    def __repr__(self):
        return 'Quote({}, {}, {}, {})'.format(self.quote_text, self.book_title, self.author, str(self.tags))

    def __str__(self):
        self.format_string = textwrap.fill(self.quote_text) + '\n\n' + textwrap.fill('-- ' + self.author + ' ' + self.book_title)
        return self.format_string
