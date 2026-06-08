# program_01_Library_management.py

class Library:

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author

    def display(self):
        print("Book Name :", self.book_name)
        print("Author :", self.author)


book1 = Library("Python Basics", "ABC")
book2 = Library("Flask Guide", "XYZ")

book1.display()
print("----------------")
book2.display()