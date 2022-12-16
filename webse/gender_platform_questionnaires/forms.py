from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#International Women's Day. Questionnaires
class QuestionnaireForm_1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_1_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_1_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

class ChatFormQuestionnaire(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')    