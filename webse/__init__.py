from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SECRET_KEY'] = '1dfc4dedcdsdsd5b2ffa3a090dfc34f845fd'
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'se_course': DBVAR, 'gd_course': DBVAR , 'gender_platform': DBVAR, 'se_platform': DBVAR}

# DBVAR = 'sqlite:///user.db'
# application.config['SECRET_KEY'] = '1dfc4dedcdsdsd5b2ffa3a090dfc34f845fd'
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
# application.config['SQLALCHEMY_BINDS'] ={'se_course': 'sqlite:///se_course.db', 'gd_course': 'sqlite:///gd_course.db', 'gender_platform': 'sqlite:///gender_platform.db', 'se_platform': 'sqlite:///se_platform.db'}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'forward_users.forward_users_login'
login_manager.login_message_category = 'info'

from webse.forward_home.routes import forward_home
from webse.forward_users.routes import forward_users
from webse.se_course_routes.routes import se_course
from webse.se_course_announcements.routes import se_course_announcements
from webse.se_course_users.routes import se_course_users
from webse.se_course_app_module.routes import se_course_app_module
from webse.se_course_app_calculator.routes import se_course_app_calculator
from webse.se_course_students_apps.routes import se_course_students_apps
from webse.se_course_se_module.routes import se_course_se_module
from webse.se_course_statistics.routes import se_course_statistics
from webse.gender_platform_routes.routes import gender_platform
from webse.gender_platform_chats.routes import gender_platform_chats
from webse.gender_platform_questionnaires.routes import gender_platform_questionnaires
from webse.gd_course_routes.routes import gd_course
from webse.gd_course_chats.routes import gd_course_chats
from webse.gd_course_announcements.routes import gd_course_announcements
from webse.gd_course_app_calculator.routes import gd_course_app_calculator
from webse.gd_course_questionnaires.routes import gd_course_questionnaires
from webse.gd_course_students_apps.routes import gd_course_students_apps
from webse.gd_course_chapters.routes import gd_course_chapters
from webse.gd_course_statistics.routes import gd_course_statistics
from webse.gd_course_app_calculator_HVL_2023_student1.routes import gd_course_app_calculator_HVL_2023_student1
from webse.boilerplates.routes import boilerplates

application.register_blueprint(forward_home)
application.register_blueprint(forward_users)
application.register_blueprint(se_course)
application.register_blueprint(se_course_announcements)
application.register_blueprint(se_course_users)
application.register_blueprint(se_course_app_module)
application.register_blueprint(se_course_app_calculator)
application.register_blueprint(se_course_students_apps)
application.register_blueprint(se_course_se_module)
application.register_blueprint(se_course_statistics)
application.register_blueprint(gender_platform)
application.register_blueprint(gender_platform_chats)
application.register_blueprint(gender_platform_questionnaires)
application.register_blueprint(gd_course)
application.register_blueprint(gd_course_chats)
application.register_blueprint(gd_course_announcements)
application.register_blueprint(gd_course_app_calculator)
application.register_blueprint(gd_course_questionnaires)
application.register_blueprint(gd_course_students_apps)
application.register_blueprint(gd_course_chapters)
application.register_blueprint(gd_course_statistics)
application.register_blueprint(gd_course_app_calculator_HVL_2023_student1)
application.register_blueprint(boilerplates)
