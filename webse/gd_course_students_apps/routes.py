from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

gd_course_students_apps= Blueprint('gd_course_students_apps', __name__)

@gd_course_students_apps.route('/green_digitalization_course/gd_students_apps', methods=['GET', 'POST'])
def gd_students_apps_home(): 
    return render_template('gd_course/students_apps/gd_students_apps_home.html', title='Students Apps Home')

