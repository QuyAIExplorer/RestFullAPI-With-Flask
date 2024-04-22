from library.extension import db
from library.library_ma import BookSchema, AuthorSchema, CategorySchema
from library.model import Books, Author , Category
from flask import request, jsonify
from sqlalchemy.sql import func
import json

book_schema = BookSchema()
books_schema = BookSchema(many=True)
authors_schema = AuthorSchema(many=True)
categories_schema = CategorySchema(many=True)


# Add a new author
def add_author_service():
    data = request.json
    if (data and ('name' in data)):
        name = request.json['name']    
        try:
            new_author = Author(name)
            db.session.add(new_author)
            db.session.commit()
            return "Add successfully!"
        except IndentationError:
            db.session.rollback()
            return "Can't add author!"
    else:
        return "Request Error!"
        
# Get all authors
def get_all_authors_service():
    authors = Author.query.all()
    if authors:
        return authors_schema.jsonify(authors)
    else:
        return jsonify({"message":"Not found"}) , 404

# Get all category
def get_all_categories_service():
    categories = Category.query.all()
    if categories:
        return categories_schema.jsonify(categories)
    else:
        return jsonify({"message":"Not found"}) , 404

    
