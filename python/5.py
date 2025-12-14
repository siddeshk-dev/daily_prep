library = []

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    book = {
        "name": name,
        "author": author,
        "year": year
    }
    library.append(book)
    print("Book added!\n")
def view_books():
    if not library:
        print("No books in library.\n")
        return
    print("\n========= BOOK LIST =========")
    for i, b in enumerate(library):
        print(f"{i + 1}. {b['name']} by {b['author']} ({b['year']})")
    print("================================\n")


def  search_book():
    q = input("Enter book name to search: ")
    print("Search results:")

    found = False
    for b in library:
        if q.lower() in b['name'].lower():
            print(f"- {b['name']} by {b['author']}")
            found = True

    if not found:
        print("No book found.")
def remove_book():
    view_books()
    num = int(input("Enter book number to remove: "))
    if 1 <= num <= len(library):
        deleted = library.pop(num - 1)
        print("Removed:", deleted['name'])
    else:
        print("Invalid choice")
def menu():
    print("=====================================")
    print("        LIBRARY MANAGEMENT")
    print("=====================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")
    print("=====================================")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        
        print("Exiting program...")
        break
    else:

        print("Invalid choice!\n")
name = "naveen"
msg = "hi"
print(name + ' said "' + msg + '"')
x = 10
y = 20
x, y = y, x
print(x, y)
