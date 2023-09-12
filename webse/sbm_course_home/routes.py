from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
from webse.models import AnnouncementGD
from webse.forward_users.utils import save_picture, read_image
sbm_course= Blueprint('sbm_course', __name__)


@sbm_course.route('/sustainable_business_models_course')
def sbm_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementGD.query.order_by(AnnouncementGD.date_posted.desc()).\
        filter((AnnouncementGD.user_id==3) | (AnnouncementGD.user_id==2)).paginate(page=page, per_page=1)
    return render_template('sbm_course/sbm_course_home.html', announcements=announcements, title='Sustainable Business Models Course', func=read_image)
  