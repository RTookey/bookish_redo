from flask import request
from bookish.models.book import Book
from bookish.app import db
from flask import Blueprint


book_controller = Blueprint('book_controller', __name__)


@book_controller.route('/healthcheck')
def health_check():
    return {"status": "OK"}


@book_controller.route('/book', methods=['POST', 'GET'])
def get_all_books():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_book = Book(title=data['title'], author=data['author'], isbn=data['isbn'], quantity=data['quantity'])
            db.session.add(new_book)
            db.session.commit()
            return {"message": "New example has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        books = Book.query.order_by(Book.Author).all()
        results = [
                {
                    'id': book.id,
                    'title': book.Title,
                    'author': book.Author,
                    'isbn' : book.ISBN,
                    'copies' : book.Quantity,
                    'available' : book.Quantity - len(book.users)
                } for book in books]
        return results
    else:
        return {"error" : "request method not supported"}


@book_controller.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book not found"}
    else:
        return {'id' : book.id, 'title': book.Title, 'author': book.Author, 'isbn' : book.ISBN, 'quantity' : book.Quantity, 'available' : book.Quantity - len(book.users)}


@book_controller.route('/book/<string:name>', methods=['GET'])
def get_book_by_title(name):
    book = Book.query.filter_by(Title=name).first()
    if book is None:
        return {"error": "Book not found"}
    else:
        return {'id' : book.id, 'title': book.Title, 'author': book.Author, 'isbn' : book.ISBN, 'quantity' : book.Quantity}


@book_controller.route('/book/author/<string:author>', methods=['GET'])
def get_book_by_author(author):
    book = Book.query.filter_by(Author=author).first()
    if book is None:
        return {"error": "Book not found"}
    else:
        return {'id' : book.id, 'title': book.Title, 'author': book.Author, 'isbn' : book.ISBN, 'quantity' : book.Quantity}
