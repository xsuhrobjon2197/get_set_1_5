#3-m
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.__pages = pages
        
    def get_pages(self):
        return self.__pages
    
    def set_pages(self, new_pages):
        self.__pages = new_pages
        
b1 = Book("Python Book", 10)
print(b1)

res = b1.get_pages()
print(res)

b1.__pages = 2
print(b1.get_pages())
