# Book Store System README

## Overview
This Book Store System is a simple, console-based Python application for managing a collection of books. It allows users to add, list, mark books as read, and delete books. Additionally, it includes functionality to save the book collection to a file and load it, ensuring data persistence.

## Features
- **Add Books**: Enter details of new books (title and author).
- **List Books**: View the entire collection of books.
- **Mark Books as Read**: Update the status of books as read.
- **Delete Books**: Remove books from the collection.
- **File Storage**: Save and load the book collection to and from a file.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.

### Running the Application
Execute the script from your command line:
```sh
python3 book_store.py
```

### Using the Application
Follow the on-screen prompts to interact with the system:
1. Add a book by entering its title and author.
2. List all books to view your collection.
3. Mark a book as read by entering its title.
4. Delete a book from the collection by entering its title.
5. Exit the application by choosing the quit option.

## File Storage
- The application uses a file named `books.txt` to save the book collection.
- The file is automatically created or updated when you add, mark a book as read, or delete a book.
- When the application starts, it attempts to load the book collection from this file.



## Acknowledgements
- This project is part of the Python programming course.
- Special thanks to the course instructors and participants for their ideas and feedback.