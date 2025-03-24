# magazine.py
class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    def articles(self):
        from article import Article
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        top_authors = [author for author, count in author_counts.items() if count > 2]
        return top_authors if top_authors else None

    @classmethod
    def top_publisher(cls):
        from article import Article
        if not Article._all_articles:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag.articles()), default=None)
