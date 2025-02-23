# author.py
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        from article import Article
        return [article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        from article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None

