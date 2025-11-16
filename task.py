class Book:
    def __init__(self, title: str, author: str, pages_num: int):
        self.title = title
        self.author = author
        self.pages_num = pages_num
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value

    @property
    def pages_num(self):
        return self._pages_num
    
    @pages_num.setter
    def pages_num(self, value):
        if value > 0:
            self._pages_num = value
        else:
            raise ValueError('Число страниц должно быть положительным')

    def same_author(self):
        pass
    
    def show_book(self):

        return {'Название книги': self.title, 'Автор': self.author, 'Количество страниц': self.pages_num}
    
book_green = Book('123/', 'Грин', 1234)

# try:
#     book_2 = Book('13', 'jsfd', -1)
# except ValueError as e:
#     print(e)

if __name__ == '__main__':
    print(book_green.show_book())
