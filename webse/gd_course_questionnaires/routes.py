import json
from flask import render_template, url_for, Blueprint, request, redirect, flash, jsonify
from webse import application, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from webse.gd_course_questionnaires.forms import QuestionnaireForm_1_q1, QuestionnaireForm_1_q2, QuestionnaireForm_1_q3, QuestionnaireForm_1_q4, ChatFormQuestionnaire
from webse.models import QuestionnaireGD, QuestionnaireGDChat, User
from webse.forward_users.utils import read_image
gd_course_questionnaires= Blueprint('gd_course_questionnaires', __name__)


@gd_course_questionnaires.route('/green_digitalization_course/questionnaire/q1', methods=['GET', 'POST'])
@login_required
def gd_course_questionnaire_q1():
    form_1_q1 = QuestionnaireForm_1_q1()
    if form_1_q1.validate_on_submit():
        QuestionnaireGD.query.filter_by(author=current_user). \
            filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
            filter(QuestionnaireGD.title_question == 'Question 1'). \
            filter(QuestionnaireGD.university == 'none'). \
            filter(QuestionnaireGD.question_num == 1).delete()
        db.session.commit()
        questionnaire = QuestionnaireGD(question_str=form_1_q1.type.data, author = current_user)
        if questionnaire.question_str == 'Bus':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Car':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Plane':
            questionnaire.question_option = 3 
        elif questionnaire.question_str == 'Ferry':
            questionnaire.question_option = 4   
        elif questionnaire.question_str == 'Scooter':
            questionnaire.question_option = 5    
        elif questionnaire.question_str == 'Bicycle':
            questionnaire.question_option = 6    
        elif questionnaire.question_str == 'Motorbike':
            questionnaire.question_option = 7  
        elif questionnaire.question_str == 'Walk':
            questionnaire.question_option = 8           
        else:
            questionnaire.question_option = 9 
        questionnaire.title_questionnaire = 'Questionnaire'
        questionnaire.title_question = 'Question 1'
        questionnaire.question_num = 1
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 1 has been submitted! Now, it is time to answer question 2', 'success')
        return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_q2'))
    return render_template('gd_course/questionnaires/gd_course_questionnaire_q1.html', title='Questionnaire, q1', form_1_q1=form_1_q1) 

@gd_course_questionnaires.route('/green_digitalization_course/questionnaire/q2', methods=['GET', 'POST'])
@login_required
def gd_course_questionnaire_q2():
    form_1_q2 = QuestionnaireForm_1_q2()
    if form_1_q2.validate_on_submit():
        QuestionnaireGD.query.filter_by(author=current_user). \
            filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
            filter(QuestionnaireGD.title_question == 'Question 2'). \
            filter(QuestionnaireGD.university == 'none'). \
            filter(QuestionnaireGD.question_num == 2).delete()
        db.session.commit()
        questionnaire = QuestionnaireGD(question_str=form_1_q2.type.data, author = current_user)
        if questionnaire.question_str == 'Bus':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Car':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Plane':
            questionnaire.question_option = 3 
        elif questionnaire.question_str == 'Ferry':
            questionnaire.question_option = 4   
        elif questionnaire.question_str == 'Scooter':
            questionnaire.question_option = 5    
        elif questionnaire.question_str == 'Bicycle':
            questionnaire.question_option = 6    
        elif questionnaire.question_str == 'Motorbike':
            questionnaire.question_option = 7  
        elif questionnaire.question_str == 'Walk':
            questionnaire.question_option = 8           
        else:
            questionnaire.question_option = 9 
        questionnaire.title_questionnaire = 'Questionnaire'
        questionnaire.title_question = 'Question 2'
        questionnaire.question_num = 2
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 2 has been submitted! Now, it is time to answer question 3', 'success')
        return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_q3'))
    return render_template('gd_course/questionnaires/gd_course_questionnaire_q2.html', title='Questionnaire, q2', form_1_q2=form_1_q2)     

@gd_course_questionnaires.route('/green_digitalization_course/questionnaire/q3', methods=['GET', 'POST'])
@login_required
def gd_course_questionnaire_q3():
    form_1_q3 = QuestionnaireForm_1_q3()
    if form_1_q3.validate_on_submit():
        QuestionnaireGD.query.filter_by(author=current_user). \
            filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
            filter(QuestionnaireGD.title_question == 'Question 3'). \
            filter(QuestionnaireGD.university == 'none'). \
            filter(QuestionnaireGD.question_num == 3).delete()
        db.session.commit()
        questionnaire = QuestionnaireGD(question_str=form_1_q3.type.data, author = current_user)
        if questionnaire.question_str == 'Bus':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Car':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Plane':
            questionnaire.question_option = 3 
        elif questionnaire.question_str == 'Ferry':
            questionnaire.question_option = 4   
        elif questionnaire.question_str == 'Scooter':
            questionnaire.question_option = 5    
        elif questionnaire.question_str == 'Bicycle':
            questionnaire.question_option = 6    
        elif questionnaire.question_str == 'Motorbike':
            questionnaire.question_option = 7  
        elif questionnaire.question_str == 'Walk':
            questionnaire.question_option = 8           
        else:
            questionnaire.question_option = 9 
        questionnaire.title_questionnaire = 'Questionnaire'
        questionnaire.title_question = 'Question 3'
        questionnaire.question_num = 3
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 3 has been submitted! Now, it is time to answer question 4', 'success')
        return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_q4'))
    return render_template('gd_course/questionnaires/gd_course_questionnaire_q3.html', title='Questionnaire, q3', form_1_q3=form_1_q3)   

@gd_course_questionnaires.route('/green_digitalization_course/questionnaire/q4', methods=['GET', 'POST'])
@login_required
def gd_course_questionnaire_q4():
    form_1_q4 = QuestionnaireForm_1_q4()
    if form_1_q4.validate_on_submit():
        QuestionnaireGD.query.filter_by(author=current_user). \
            filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
            filter(QuestionnaireGD.title_question == 'Question 4'). \
            filter(QuestionnaireGD.university == 'none'). \
            filter(QuestionnaireGD.question_num == 4).delete()
        db.session.commit()
        questionnaire = QuestionnaireGD(question_str=form_1_q4.type.data, author = current_user)
        if questionnaire.question_str == 'Bus':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Car':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Plane':
            questionnaire.question_option = 3 
        elif questionnaire.question_str == 'Ferry':
            questionnaire.question_option = 4   
        elif questionnaire.question_str == 'Scooter':
            questionnaire.question_option = 5    
        elif questionnaire.question_str == 'Bicycle':
            questionnaire.question_option = 6    
        elif questionnaire.question_str == 'Motorbike':
            questionnaire.question_option = 7  
        elif questionnaire.question_str == 'Walk':
            questionnaire.question_option = 8           
        else:
            questionnaire.question_option = 9 
        questionnaire.title_questionnaire = 'Questionnaire'
        questionnaire.title_question = 'Question 4'
        questionnaire.question_num = 4
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 4 has been submitted! Now, it is time to participate in the debate.', 'success')
        return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_summary'))
    return render_template('gd_course/questionnaires/gd_course_questionnaire_q4.html', title='Questionnaire, q4', form_1_q4=form_1_q4)  

@gd_course_questionnaires.route('/green_digitalization_course/questionnaire/summary', methods=['GET', 'POST'])
@login_required
def gd_course_questionnaire_summary():
    # Question 1
    q1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    q1_Bus = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 1). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q1[0]=q1_Bus

    q1_Car = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 2). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q1[1]=q1_Car

    q1_Plane = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 3). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q1[2]=q1_Plane   

    q1_Ferry = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 4). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q1[3]=q1_Ferry 

    q1_Scooter = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 5). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q1[4]=q1_Scooter

    q1_Bicycle = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 6). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q1[5]=q1_Bicycle
    
    q1_Motorbike = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 7). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q1[6]=q1_Motorbike

    q1_Walk = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 8). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q1[7]=q1_Walk

    q1_Other = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 1).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 9). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q1[8]=q1_Other

    # Question 2
    q2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    q2_Bus = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 1). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q2[0]=q2_Bus

    q2_Car = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 2). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q2[1]=q2_Car

    q2_Plane = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 3). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q2[2]=q2_Plane   

    q2_Ferry = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 4). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q2[3]=q2_Ferry 

    q2_Scooter = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 5). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q2[4]=q2_Scooter

    q2_Bicycle = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 6). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q2[5]=q2_Bicycle
    
    q2_Motorbike = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 7). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q2[6]=q2_Motorbike

    q2_Walk = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 8). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q2[7]=q2_Walk

    q2_Other = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 2).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 9). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q2[8]=q2_Other

    # Question 3
    q3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    q3_Bus = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 1). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q3[0]=q3_Bus

    q3_Car = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 2). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q3[1]=q3_Car

    q3_Plane = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 3). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q3[2]=q3_Plane   

    q3_Ferry = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 4). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q3[3]=q3_Ferry 

    q3_Scooter = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 5). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q3[4]=q3_Scooter

    q3_Bicycle = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 6). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q3[5]=q3_Bicycle
    
    q3_Motorbike = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 7). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q3[6]=q3_Motorbike

    q3_Walk = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 8). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q3[7]=q3_Walk

    q3_Other = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 3).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 9). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q3[8]=q3_Other

    # Question 4
    q4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    q4_Bus = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 1). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q4[0]=q4_Bus

    q4_Car = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 2). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q4[1]=q4_Car

    q4_Plane = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 3). \
        order_by(QuestionnaireGD.question_num.asc()).count()
    q4[2]=q4_Plane   

    q4_Ferry = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 4). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q4[3]=q4_Ferry 

    q4_Scooter = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 5). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q4[4]=q4_Scooter

    q4_Bicycle = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 6). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q4[5]=q4_Bicycle
    
    q4_Motorbike = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 7). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q4[6]=q4_Motorbike

    q4_Walk = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 8). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q4[7]=q4_Walk

    q4_Other = QuestionnaireGD.query.filter(QuestionnaireGD.question_num == 4).\
        filter(QuestionnaireGD.title_questionnaire == 'Questionnaire'). \
        filter(QuestionnaireGD.university == 'none').filter(QuestionnaireGD.question_option == 9). \
        order_by(QuestionnaireGD.question_num.asc()).count()  
    q4[8]=q4_Other

    page = request.args.get('page', 1, type=int)
    chats = QuestionnaireGDChat.query.filter(QuestionnaireGDChat.university == 'none').\
        order_by(QuestionnaireGDChat.date_chat.desc()).paginate(page=page, per_page=3)        
  
    return render_template('gd_course/questionnaires/gd_course_questionnaire_summary.html', title='Questionnaire, summary',
        q1_results=json.dumps(q1), q2_results=json.dumps(q2), q3_results=json.dumps(q3), q4_results=json.dumps(q4),
        chats=chats, func=read_image)            

@gd_course_questionnaires.route('/green_digitalization_course/questionnaire/summary/chat', methods=['GET', 'POST'])
@login_required
def gd_course_questionnaires_summary_chat():
    form = ChatFormQuestionnaire()
    if form.validate_on_submit():
        chat = QuestionnaireGDChat(title_chat=form.title.data, content=form.content.data, author=current_user,
                    university='none')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_summary'))
    return render_template('gd_course/questionnaires/gd_course_questionnaire_create_chat.html', title='Questionnaire - Chat',
                           form=form, legend='Questionnaire')  


# These routes are common for all the chats
@gd_course_questionnaires.route("/green_digitalization_course/questionnaire/summary/chat/<int:chat_id>") 
def chat(chat_id):
    chat = QuestionnaireGDChat.query.get_or_404(chat_id)
    return render_template('gd_course/questionnaires/gd_course_questionnaire_chat.html', title=chat.title_chat, chat=chat, func=read_image)    

@gd_course_questionnaires.route("/green_digitalization_course/questionnaire/summary/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat(chat_id):
    chat = QuestionnaireGDChat.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatFormQuestionnaire()
    if form.validate_on_submit():
        chat.title_chat=form.title.data
        chat.content=form.content.data
        db.session.commit()
        flash('Your chat has been updated!', 'success')
        return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_summary'))
    elif request.method == 'GET':
        form.title.data = chat.title_chat
        form.content.data = chat.content
    return render_template('gd_course/questionnaires/gd_course_questionnaire_create_chat.html', title='Update Chat',
                           form=form, legend='Update Chat')    

@gd_course_questionnaires.route("/green_digitalization_course/questionnaire/summary/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = QuestionnaireGDChat.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('gd_course_questionnaires.gd_course_questionnaire_summary'))   

@gd_course_questionnaires.route("/green_digitalization_course/questionnaire/summary/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = QuestionnaireGDChat.query.filter_by(author=user)\
        .order_by(QuestionnaireGDChat.date_chat.desc())\
        .paginate(page=page, per_page=2)
    return render_template('gd_course/questionnaires/gd_course_questionnaire_user_chats.html', chats=chats, user=user, func=read_image)                              
