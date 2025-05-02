from bookish.app import db
from bookish.models.user_book import user_book


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String())
    Author = db.Column(db.String())
    ISBN = db.Column(db.String())
    Quantity = db.Column(db.Integer)
    users = db.relationship('User', secondary=user_book, back_populates='books')

    def __init__(self, title, author, isbn, quantity):
        self.Title = title
        self.Author = author
        self.ISBN = isbn
        self.Quantity = quantity


    def serialize(self):
        return {
            'id': self.id,
            'Title': self.Title,
            'Author': self.Author,
            'ISBN': self.ISBN,
            'Quantity': self.Quantity,
        }
