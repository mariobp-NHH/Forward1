from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.gd_course_chapters.forms import ModulsForm_gdc_ch1_q1, ModulsForm_gdc_ch1_q2, ModulsForm_gdc_ch1_q3
from webse.gd_course_chapters.forms import ModulsForm_gdc_ch2_q1, ModulsForm_gdc_ch2_q2, ModulsForm_gdc_ch2_q3, ModulsForm_gdc_ch2_q4, ModulsForm_gdc_ch2_q5, ModulsForm_gdc_ch2_q6

gd_course_chapters= Blueprint('gd_course_chapters', __name__)

@gd_course_chapters.route('/green_digitalization_course/chapter1', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch1(): 
    form_gdc_ch1_q1 = ModulsForm_gdc_ch1_q1()
    form_gdc_ch1_q2 = ModulsForm_gdc_ch1_q2()
    form_gdc_ch1_q3 = ModulsForm_gdc_ch1_q3()

    if form_gdc_ch1_q1.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch1'). \
            filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
            filter(ModulsGD.question_num == 1).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch1_q1.type.data, author=current_user)
        if moduls.question_str == 'Add Python to environmental variables':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch1'
        moduls.title_ch = 'Chapter 1. Installation and First Flask App'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'ch1'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch1'))

    if form_gdc_ch1_q2.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch1'). \
            filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch1_q2.type.data, author=current_user)
        if moduls.question_str == 'Installing the basic tools in your virtual environment to run your first app':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch1'
        moduls.title_ch = 'Chapter 1. Installation and First Flask App'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'ch1'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch1'))

    if form_gdc_ch1_q3.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch1'). \
            filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch1_q3.type.data, author=current_user)
        if moduls.question_str == 'Both lines of code':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch1'
        moduls.title_ch = 'Chapter 1. Installation and First Flask App'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'ch1'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch1'))    
    return render_template('gd_course/chapters/ch1.html', title='Green Digitalization Course, ch1',
        form_gdc_ch1_q1=form_gdc_ch1_q1, form_gdc_ch1_q2=form_gdc_ch1_q2, form_gdc_ch1_q3=form_gdc_ch1_q3)

#Chapter 2
@gd_course_chapters.route('/green_digitalization_course/chapter2', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch2(): 
    form_gdc_ch2_q1 = ModulsForm_gdc_ch2_q1()
    form_gdc_ch2_q2 = ModulsForm_gdc_ch2_q2()
    form_gdc_ch2_q3 = ModulsForm_gdc_ch2_q3()
    form_gdc_ch2_q4 = ModulsForm_gdc_ch2_q4()
    form_gdc_ch2_q5 = ModulsForm_gdc_ch2_q5()
    form_gdc_ch2_q6 = ModulsForm_gdc_ch2_q6()

    if form_gdc_ch2_q1.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 1).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q1.type.data, author=current_user)
        if moduls.question_str == 'render_template':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))

    if form_gdc_ch2_q2.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q2.type.data, author=current_user)
        if moduls.question_str == '<title>{{title}}</title>':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))

    if form_gdc_ch2_q3.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q3.type.data, author=current_user)
        if moduls.question_str == '<ul><li>...</li></ul>':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))    

    if form_gdc_ch2_q4.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 4).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'url_for':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))   

    if form_gdc_ch2_q5.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 5).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'Jinja2 is the Flask template engine that allows us to render variables and logical statements in our html files':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))  

    if form_gdc_ch2_q6.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 6).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q4.type.data, author=current_user)
        if moduls.question_str == '{% block content %} {% endblock %}':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))          
    return render_template('gd_course/chapters/ch2.html', title='Green Digitalization Course, ch2',
        form_gdc_ch2_q1=form_gdc_ch2_q1, form_gdc_ch2_q2=form_gdc_ch2_q2, form_gdc_ch2_q3=form_gdc_ch2_q3,
        form_gdc_ch2_q4=form_gdc_ch2_q4, form_gdc_ch2_q5=form_gdc_ch2_q5, form_gdc_ch2_q6=form_gdc_ch2_q6)
