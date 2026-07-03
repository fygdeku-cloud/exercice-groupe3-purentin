class Book:
    def __init__(self, title: str, author: str):
        self.title = title.strip()
        self.author = author.strip()
        self.is_available = True  # True means available, False means borrowed

    def borrow_book(self) -> bool:
        if self.is_available:
            self.is_available = False
        return True

    def return_book(self) -> bool:
        if not self.is_available:
            self.is_available = True
        return True


