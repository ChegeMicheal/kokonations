from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'users'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TRIAL KEY'

    #sqlite database
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MYSQLpassword24@localhost/user'

    #jawsDB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mgewt9r4y3xqrzx9:tic4d2e6fe79vw98@d1kb8x1fu8rhcnej.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/c60lhk7e30osyo5v'

    #Postgresql
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://u77ffnfeb72asn:pfa57c28b81fd1e85ee274336be11f7b0a49e63cb3d8e19d63a6763cf6f195e44@c5p86clmevrg5s.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d13aoi9fe4joeus'
    db.init_app(app)
    
    from .views import views
    from.auth import auth
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    from .models import User,Review
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('database created!')
            
            #database_fatal_error ...(remove this after deployment)
            #db.drop4all(#error)
            #print('oops! database dropped successfully!')

        