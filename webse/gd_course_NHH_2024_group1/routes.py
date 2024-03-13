from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2024_group1.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, TrainForm, ElkickScooterForm, ElBicycleForm
from datetime import timedelta, datetime
from webse import db, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json

gd_course_NHH_2024_group1=Blueprint('gd_course_NHH_2024_group1',__name__)

#Home routes
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/home')
def home_home():
  return render_template('gd_course/NHH_2024_group1/home.html', title = 'Home')

#Users routes
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_NHH_2024_group1=.home_home'))
    return render_template('gd_course/NHH_2024_group1/users/register.html', title='Register', form=form)

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'fjell@demo.com' and form.password.data == 'regn':
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect(url_for('gd_course_NHH_2024_group1=.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/NHH_2024_group1/users/login.html', title='Login', form=form)

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/logout')
def logout():
  logout_user()
  return redirect(url_for('gd_course_NHH_2024_group1.home_home'))

# Methodology
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2024_group1/methodology.html', title='Methodology')


#Carbon app, main page
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_app')
#@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2024_group1/carbon_app/carbon_app.html', title='carbon_app')

