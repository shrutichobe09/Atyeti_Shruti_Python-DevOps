class book:
    def __init__(self, title):
        self.title=title

    def read(self):
        print(f"reading the book: {self.title}")
    
class Ebook(book):
    def download(self):
        print(f"downloading the book: {self.title}")

Ebook1=Ebook("Kaizen")
Ebook1.read()
Ebook1.download()