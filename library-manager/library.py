from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str):
        new_book = Book(title, author)
        self.books.append(new_book)
        print('Le livre',title,' a ete ajoute')

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        
        if not available_books:
            print("Aucun disponible dans cette library")

        print("\n--- Livres Disponibles ---")
        for index, book in enumerate(available_books, start=1):
            print(index, book.title,' de ',book.author)

    def borrow_book(self, title: str):
        for book in self.books:
            if book.title == title:
                if book.borrow_book():
                    print("Vous avez reussi l'emprunt de",book.title)
                else:
                    print("L emprunt du livre ",book.title,"a echoue")

    def return_book(self, title: str):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    print("Vous avez retorne",book.title)
                else:
                    print("Impossible de retorner le livre ",book.title)
                    
        print("Le livre: ",title, "ne se trouve pas dans cette library")


