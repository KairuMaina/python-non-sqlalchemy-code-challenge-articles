class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        self.name = name
        self.category = category
