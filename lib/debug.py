# Assuming your classes are defined in the same file or another module
from your_module import Author, Magazine, Article  # Replace 'your_module' with your actual file name

# Now, instantiate the classes with sample data
author = Author("J.K. Rowling")
magazine = Magazine("Time", "News")
article = Article(author, magazine, "The Magic of Harry Potter")

# Place this code before entering the debugger
ipdb.set_trace()  # Enter debugging mode
