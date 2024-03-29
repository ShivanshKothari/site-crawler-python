from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    url = parse.urljoin(self.base_url, attr[1])
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        print(message)
