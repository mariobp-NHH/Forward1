from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#Chapter 2
class SpotGo_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('option a',
                                 'option a'),
                                ('option b',
                                 'option b'),
                                ('option c',
                                 'option c')])
    submit = SubmitField('Submit')  

class SpotGo_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('option aa',
                                 'option aa'),
                                ('option bb',
                                 'option bb'),
                                ('option cc',
                                 'option cc')])
    submit = SubmitField('Submit')    

class SpotGo_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('option aaa',
                                 'option aaa'),
                                ('option bbb',
                                 'option bbb'),
                                ('option ccc',
                                 'option ccc')])
    submit = SubmitField('Submit') 

class SpotGo_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('option aaaa',
                                 'option aaaa'),
                                ('option bbbb',
                                 'option bbbb'),
                                ('option cccc',
                                 'option cccc')])
    submit = SubmitField('Submit')      