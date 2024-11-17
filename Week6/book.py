
class Book(object):
    """superclass
    """

    def __init__(self, title, quantity, author, price):
        # public property
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        # private property(encapsulation): Encapsulation is the process 
        # of preventing clients from accessing certain properties,
        # which can only be accessed through specific methods.
        self._discount = 50
    
    def print_title(self):
        print("The title is: {}".format(self.title))
        # print private property only if called such as below
        print("The discount is: {}".format(self._discount))

        
class Customer(object):
    def __init__(self):
        pass
    
class Novel(Book):
    """subclass
    """
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    """subclass
    """
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch