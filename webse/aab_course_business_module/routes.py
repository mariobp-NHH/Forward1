from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
from webse.models import AnnouncementGD
from webse.forward_users.utils import save_picture, read_image
aab_course_business_module= Blueprint('aab_course_business_module', __name__)

# Business module
@aab_course_business_module.route('/sustainable_business_models_course/business_module')
def aab_course_business_module_home():
    return render_template('aab_course/aab_business_module/business_module_home.html', title='Sustainable Business Models Course, App Module')
  
#Chapter 1
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/chapter1')
def ch1(): 
    return render_template('aab_course/aab_business_module/chapters/ch1.html', title='Auditing, Accounting and Business Course, Business Module,  ch1')   

#Chapter 2
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/chapter2')
def ch2(): 
    return render_template('aab_course/aab_business_module/chapters/ch2.html', title='Auditing, Accounting and Business Course, Business Module, ch2') 

#Chapter 3
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/chapter3')
def ch3(): 
    return render_template('aab_course/aab_business_module/chapters/ch3.html', title='Auditing, Accounting and Business Course, Business Module, ch3') 
  
