import requests
from bs4 import BeautifulSoup as bs

class TimPool():
    def __init__(self, article_titles: list = []):
        """Initializes the class."""
        self.article_titles = article_titles

        self._url = 'https://timcast.com/channel/timcast-irl/page'
        
        for i in range(4):
            _u = f'{self._url}/{i}'
            _data = bs(requests.get(_u).text, 'html.parser')
            self.get_headlines(data=_data)

    def get_headlines(self, data: str) -> list:
        """Returns the headlines from the Timcast IRL website."""
        _articles = data.findAll("div", {"class", "article"})
        for article in _articles:
            if article.h2 is not None:
                _art = article.h2.text
                if "|" in _art:
                    _art = _art.split("|")[0].rstrip()
                elif "#" in _art:
                    _art = _art.split("#")[0].rstrip()

                if "-" in _art:
                    _art = _art.split("-")[1].lstrip()

                self.article_titles.append(_art)
