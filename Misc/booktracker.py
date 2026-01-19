library = []



def add_book_to_library():
    title = input("What is the book title? (enter 0 to end this process) ")
    if title == "0":
        return False
    author = input("Who is the book author?")
    year = int(input("What year was the book published?"))

    book = {
    "title": title,
    "author": author,
    "year": year
    }

    library.append(book)
    return True

def view_specific_book(book_number):
    book = library[book_number - 1]
    print(book)

while True:
    if not add_book_to_library():
        break

open_library = input("Would you like to see a specific book from the library? (yes/no only)")
if open_library == "yes":
    while True:
        book_number = int(input("What is the book number? (enter 0 to end this process) "))
        if book_number == 0:
            break

        if 1 <= book_number <= len(library):
            view_specific_book(book_number)
        else:
            print("Invalid book number.")
print(len(library))
view_all = input("Would you like to print all books in a list? (yes/no only)")
if view_all == "yes":
    for book in library:
            print(f"Title: {book["title"]}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
