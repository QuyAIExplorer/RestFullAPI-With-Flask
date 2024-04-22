from flask import Blueprint
from .service import get_all_authors_service, get_all_categories_service, add_author_service
# Create a supportive flask server to serve the main flask server
author= Blueprint("author",__name__)
category= Blueprint("category",__name__)

# endpoint to access book asset | get all authors
@author.route("/author-management/authors", methods = ['GET'])
def get_all_authors():
    return get_all_authors_service()

# endpoint to access book asset | get all categories
@category.route("/category-management/categories", methods = ['GET'])
def get_all_categories():
    return get_all_categories_service()

# endpoint to access book asset | get all authors
@author.route("/author-management/author", methods = ['POST'])
def add_new_author():
    return add_author_service()