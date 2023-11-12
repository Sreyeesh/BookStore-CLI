# Book Store System

# In-memory storage for books
books = []

# Functions

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    save_books()

def list_books():
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, Read: {read}")

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            break
    save_books()

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]
    save_books()

def save_books():
    with open('books.txt', 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

def load_books():
    try:
        with open('books.txt', 'r') as file:
            lines = file.readlines()
            global books
            books = [
                {'name': line.split(',')[0], 'author': line.split(',')[1], 'read': line.split(',')[2].strip() == 'True'}
                for line in lines
            ]
    except FileNotFoundError:
        pass  # If file not found, start with an empty books list

# Main Interface

def menu():
    load_books()
    while True:
        print("\nBook Store")
        print("1. Add a book")
        print("2. List all books")
        print("3. Mark a book as read")
        print("4. Delete a book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the book name: ")
            author = input("Enter the author name: ")
            add_book(name, author)

        elif choice == '2':
            list_books()

        elif choice == '3':
            name = input("Enter the book name you just finished reading: ")
            mark_book_as_read(name)

        elif choice == '4':
            name = input("Enter the book name to delete: ")
            delete_book(name)

        elif choice == '5':
            break
        else:
            print("Invalid choice, please choose again.")

# Running the menu function
if __name__ == '__main__':
    menu()
