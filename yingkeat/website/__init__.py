from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from os import path
from flask_login import LoginManager
from flask_mail import Mail,Message

db = SQLAlchemy()
DB_NAME = "database.db"
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'miniitproject'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Configure Flask-Mail settings
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'your_email@example.com'
    app.config['MAIL_PASSWORD'] = 'your_email_password'
    app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

    db.init_app(app)
    mail.init_app(app)

    # Initialize Flask-Migrate
    from .models import User, Club, Review
    migrate = Migrate(app, db)  # Initialize Migrate with app and db

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print("Database is created!")

