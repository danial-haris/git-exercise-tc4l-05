from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

db = SQLAlchemy()
Admin = Admin()

def admin_page():
    app = Flask(__name__)
    app.config("SQLALCHEMY_DATABASE_URL") == "sqlite:///db.sqlite3"

    db.init_app(app)
    Admin.init_app(app)

    return app
