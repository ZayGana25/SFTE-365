

import os
os.system("cls")

# from 'file name' import 'class names'
from book import Book, Customer, Novel, Academic


def main():
    print("Object-Oriented Programming in Python")
    
    book1 = Book("OOP using Python","my quantity","my author","price")
    book1.print_title()
    
    
    customer1 = Customer
    
    novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
    novel1.print_title()
    # novel1.set_discount(0.20)

    academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')
    academic1.print_title()

    print(novel1)
    print(academic1)
    
if __name__ == '__main__':
    main()