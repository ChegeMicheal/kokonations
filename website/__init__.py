from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'users'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TRIAL KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MYSQLpassword24@localhost/user'
    db.init_app(app)
    
    from .views import views
    from.auth import auth
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    from .models import Member
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return Member.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('database created!')
            
            #database_fatal_error ...(remove this after deployment)
            #db.drop_all()
            #print('database dropped!')

        