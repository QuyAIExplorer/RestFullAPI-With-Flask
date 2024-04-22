from library.extension import db
from library.library_ma import BookSchema
from library.model import Books, Author, Category, Borrow, Students
from flask import request, jsonify
from sqlalchemy.sql import func
import json


# Get books a student brrowed
def get_borrow_author_cat_service(student_name):
    borrows = db.session.query(Borrow.id, Books.name, Category.name, Author.name).join(Students, Borrow.student_id == Students.id).join(Books, Borrow.book_id == Books.id).join(
        Category, Books.category_id == Category.id).join(Author, Books.author_id == Author.id).filter(func.lower(Students.name) == student_name.lower()).all()
    if borrows:
        return jsonify({f"{student_name} borrowed": borrows}), 200
    else:
        return jsonify({"message": "Not found borrow!"}), 404