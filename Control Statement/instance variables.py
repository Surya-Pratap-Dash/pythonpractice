from pprint import pprint

class HtmlDocument:
    version = 5
    extension = 'html'

pprint(HtmlDocument.__dict__)
print(HtmlDocument.extension)
print(HtmlDocument.version)
