import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt, DBVAR
from webse.models import  Moduls
from flask_login import login_user, current_user, logout_user, login_required

aab_course_statistics = Blueprint('aab_course_statistics', __name__)

@aab_course_statistics.route('/sustainable_business_models_course/business_module/statistics', methods=['GET', 'POST'])
@login_required
def statistics_main():
    return render_template('aab_course/aab_business_module/statistics/statistics.html')

@aab_course_statistics.route('/sustainable_business_models_course/business_module/statistics/ch1', methods=['GET', 'POST'])
@login_required
def ch1():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='AAB Course Business Module'). \
        filter(Moduls.title_ch=='Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='AAB Course Business Module'). \
        filter(Moduls.title_ch=='Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='AAB Course Business Module'). \
        filter(Moduls.title_ch=='Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()
    
    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    flash('Your answer has been submitted!', 'success')
    return render_template('aab_course/aab_business_module/statistics/ch1.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1 =correct_q1, incorrect_q1=incorrect_q1, correct_q2 =correct_q2, incorrect_q2=incorrect_q2)

