# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,bid=None,bname=None,price=None,author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def ShowBook(self):
        print(f'Bid:{self.bid}\tBname:{self.bname}\tPrice:{self.price}\tAuthor:{self.author}\n')

    def __del__(self):
        print('Book object Destructed')

b1 = Book()

b1.bid = 101
b1.bname = "Python"
b1.price = 500
b1.author = "Guido"

b2 = Book(102, "Java", 600, "James")
print("Book 1 details:")
b1.ShowBook()
print("\nBook 2 details:")
b2.ShowBook()

    