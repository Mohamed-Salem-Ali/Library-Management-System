# class book 
# attributes id,title,author,genre,available
class Book:
    def __init__(self, book_id, title, author, genre, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def __str__(self):
        return f"{self.book_id} - {self.title}"