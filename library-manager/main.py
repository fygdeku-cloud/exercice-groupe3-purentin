from library import Library

def main():
    # Instantiate the central library system
    my_library = Library()

    while True:
        print("\n=============================")
        print("  LIBRARY MANAGER ")
        print("=============================")
        print("1. Ajouter un nouveau livre")
        print("2. Liste des livres disponibles")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Sortir de l'appli")
        print("=============================")
        
        choice = input("Entrer votre choix (1-5): ").strip()

        if choice == "1":
            title = input("Entrer un titre: ").strip()
            author = input("Enter le nom de l'auteur de ce livre: ").strip()
            if title and author:
                my_library.add_book(title, author)
            else:
                print("Le titre ou le nom de l'auteur est vide")

        elif choice == "2":
            my_library.list_available_books()

        elif choice == "3":
            title = input("Entrer le titre du livre a emprunter: ").strip()
            if title:
                my_library.borrow_book(title)

        elif choice == "4":
            title = input("Entrer le titre du livre a renvoyer: ").strip()
            if title:
                my_library.return_book(title)

        elif choice == "5":
            print("Sortir de l'application ===================")
            break

        else:
            print("Le choix entre n'est pas valide. Entre un choix compris entre 1 et 5")

if __name__ == "__main__":
    main()