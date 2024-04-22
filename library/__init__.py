from flask import Flask 
from .books.controller import books
from flask_cors import CORS
from .borrow.controller import borrow
from .author_category.controller import author,category
from .extension import db, ma
from .model import Students, Books, Borrow, Author, Category
import os

""" Khi sử dụng db.create_all(app=app) trong hàm create_db, 
SQLAlchemy sẽ tự động quét tất cả các lớp db.Model đã được định nghĩa và tạo bảng cho mỗi lớp mô hình đó trong cơ sở dữ liệu."""

        
def create_app(config = "config.py"):
    app = Flask(__name__)
    CORS(app)
    app.config.from_pyfile(config)
    
    db.init_app(app)
    
    ma.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(books)
    app.register_blueprint(borrow)
    app.register_blueprint(author)
    app.register_blueprint(category)
    return app