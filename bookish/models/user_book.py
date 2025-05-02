from bookish.app import db
import datetime

user_book = db.Table('user_book',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('date_added', db.DateTime, default=datetime.datetime.now()),
    db.Column('date_due', db.DateTime, default=datetime.datetime.now())
)
