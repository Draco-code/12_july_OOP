class Book:
    def __init__(self, name : str = "", pages: int = 0, price: int = 0)   -> None:
        self.name = name
        self.pages = pages
        self.price = price

    def get_price(self):
        return self.price
    def get_pages(self):
        return self.pages
    def set_name(self, new_name: str):
        self.name = new_name
    def set_price(self, new_price: int):
        self.price = new_price
    def set_pages(self, new_pages: int):
        self.pages = new_pages
    
    def __str__(self) -> str:
         return f"""
Name: {self.name}
Pages: {self.pages}
Price: ${self.price}"""


# b1 = Book('Harry Potter', 200, 100)
# b2 = Book('The Hobbit', 80, 150)
# b3 = Book('To Kill a Mockingbird', 91, 120)
# b4 = Book('1984', 50, 180)
# b5 = Book('Pride and Prejudice', 432, 250)

b1, b2, b3, b4, b5 = Book(), Book(), Book(), Book(), Book()
books = [b1, b2, b3, b4, b5]

for idx, book in enumerate(books):
    print(f"Fill the {idx+1}th book's info:")
    book.set_name(input("Name for the {i}th book: "))
    book.set_pages(int(input("Page volume: ")))
    book.set_price(int(input("Price: ")))

for book in books:
        book.set_pages(book.get_pages()+10)
        if book.get_pages() > 100:
             book.set_price(book.get_price()//2)
        print(book)