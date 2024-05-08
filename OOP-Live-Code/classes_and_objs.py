#!/usr/bin/python3

# Define a class named Book
class Book:
    # Constructor method with parameters for title, author, and pages
    def __init__(self, title, author, pages):
        self.title = title 
        self.author = author
        self.pages = pages

    # Method to return a formatted string with book details
    # A Method is just a function within a class
    def book_details(self):
        # Return the book's title, author, and pages
        return f"| {self.title:<30} | {self.author:<20} | {self.pages:>5} |"
    

print("+---------------------------------------------------------------+")
print("|                      BOOK CATALOGUE LIST                      |")
print("+---------------------------------------------------------------+")

# Create a list of Book objects with different book details
books = [
    Book("1984", "George Orwell", 328),
    Book("To Kill a Mockingbird", "Harper Lee", 281),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 180),
    Book("The Python Bible", "Florian Dedov", 501),
    Book("Pride and Prejudice", "Jane Austen", 279)
]

# Print table header with column titles aligned and formatted
print(f"| {'Title':<30} | {'Author':<20} | {'Pages':>5} |")
# Print a separator line to visually separate the header from the data rows
print(f"+{'-'*32}+{'-'*22}+{'-'*7}+")

# Loop through each book object in the books list
for book in books:
    print(book.book_details())
    print(f"+{'-'*32}+{'-'*22}+{'-'*7}+")


print("|                      END OF CATALOGUE LIST                    |")
print("+---------------------------------------------------------------+")