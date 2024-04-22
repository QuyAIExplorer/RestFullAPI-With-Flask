from flask import Blueprint
from .service import (add_book_service, get_book_by_id_service, get_all_books_service,
                      update_book_by_id_service, delete_book_by_id_service, get_book_by_author_service)

# Create a supportive flask server to serve the main flask server
books = Blueprint("books",__name__)

# endpoint to access book asset | add a new book
@books.route("/book-management/book", methods = ['POST'])
def add_book():
    return add_book_service()

# endpoint to access book asset | get book by id
@books.route("/book-management/book/<int:id>", methods = ['GET'])
def get_book_by_id(id):
    return get_book_by_id_service(id)

# endpoint to access book asset | get all books
@books.route("/book-management/books", methods = ['GET'])
def get_all_books():
    return get_all_books_service()

# endpoint to access book asset | update book by id
@books.route("/book-management/book/<int:id>", methods = ['PUT'])
def update_book_by_id(id):
    return update_book_by_id_service(id)

# endpoint to access book asset | update book by id
@books.route("/book-management/book/<int:id>", methods = ['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_service(id)

# endpoint to access book asset | get book by author
@books.route("/book-management/book/<string:author>", methods = ['GET'])
def get_book_by_author(author):
    return get_book_by_author_service(author)

