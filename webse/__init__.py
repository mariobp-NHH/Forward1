from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
# from os import environ

application = Flask(__name__)
# application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY_HEROKU')
# application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY_HEROKU')

application.config['SECRET_KEY'] = os.getenv("SECRET_KEY_HEROKU")

#DBVAR = process.env.DATABASE_URL
DBVAR = "postgresql://spaomjipgdcsqv:06323463be5381864168727a5c780b5de930901bb1ec54ef55e9ab3788c622bc@ec2-54-77-40-202.eu-west-1.compute.amazonaws.com:5432/d6jm40e34d9jf4"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
application.config['SQLALCHEMY_BINDS'] ={'gd_course': DBVAR, 'gender_platform': DBVAR }
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'forward_users.forward_users_login'
login_manager.login_message_category = 'info'


from webse.forward_home.routes import forward_home
from webse.forward_users.routes import forward_users
# from webse.se_course_routes.routes import se_course
from webse.gender_platform_routes.routes import gender_platform
from webse.gender_platform_chats.routes import gender_platform_chats
# from webse.gender_platform_questionnaires.routes import gender_platform_questionnaires
from webse.users.routes import users
from webse.gd_course_routes.routes import gd_course
from webse.gd_course_chats.routes import gd_course_chats

application.register_blueprint(forward_home)
application.register_blueprint(forward_users)
# application.register_blueprint(se_course)
application.register_blueprint(gender_platform)
application.register_blueprint(gender_platform_chats)
# application.register_blueprint(gender_platform_questionnaires)
application.register_blueprint(users)
application.register_blueprint(gd_course)
application.register_blueprint(gd_course_chats)
