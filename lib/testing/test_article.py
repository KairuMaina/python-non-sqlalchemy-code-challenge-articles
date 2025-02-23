from lib.classes.article import Article
from lib.classes.author import Author
from lib.classes.magazine import Magazine

def test_article_creation():
    author = Author("John Doe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = Article(author, magazine, "Sample Title")
    
    assert article.title == "Sample Title"
    assert article.author == author
    assert article.magazine == magazine
