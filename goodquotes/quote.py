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
        wrapped_text = textwrap.fill(self.quote_text, 80)
        new_sentences = [sentence.ljust(80) for sentence in wrapped_text.split('\n')]
        adjusted_text = '\n'.join(new_sentences)

        self.format_string = adjusted_text + '\n\n' + textwrap.fill('-- ' + self.author + ' ' + self.book_title)
        return self.format_string
