class L:
    def __init__(self):
        self.nb = 0
        self.books = []

    def add(self , book):
        self.books.append(book)
        self.nb = len(self.books)

    def show(self):
        print(f"the books in the library are {self.nb} no of books")

l1 = L()
l1.add("harry potter")
l1.show()