class Quote(object):

    def __init__(self, quote_text, book_title, author, tags=None):
        self.quote_text = quote_text
        self.book_title = book_title
        self.author = author
        self.tags = None

    def __repr__(self):
        return 'Quote({}, {}, {}, {})'.format(self.quote_text, self.book_title, self.author, str(self.tags))
