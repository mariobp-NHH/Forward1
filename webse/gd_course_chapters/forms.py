from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class ChatForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#Chapter 1
class ModulsForm_gdc_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Associate files with Python',
                                 'Associate files with Python'),
                                ('Add Python to environmental variables',
                                 'Add Python to environmental variables'),
                                ('Create shortcuts for installed applications',
                                 'Create shortcuts for installed applications')])
    submit = SubmitField('Submit')  

class ModulsForm_gdc_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Creating the routes for your app',
                                 'Creating the routes for your app'),
                                ('Creating the functions for your routes',
                                 'Creating the functions for your routes'),
                                ('Installing the basic tools in your virtual environment to run your first app',
                                 'Installing the basic tools in your virtual environment to run your first app')])
    submit = SubmitField('Submit')    

class ModulsForm_gdc_ch1_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('@application.route(/methodology)',
                                 '@application.route(/methodology)'),
                                ('def methodology():',
                                 'def methodology():'),
                                ('Both lines of code',
                                 'Both lines of code')])
    submit = SubmitField('Submit') 

#Chapter 2
class ModulsForm_gdc_ch2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('redirect',
                                 'redirect'),
                                ('render_template',
                                 'render_template'),
                                ('submit',
                                 'submit')])
    submit = SubmitField('Submit')  

class ModulsForm_gdc_ch2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('<title>{title}</title>',
                                 '<title>{title}</title>'),
                                ('<title>(title)</title>',
                                 '<title>(title)</title>'),
                                ('<title>{{title}}</title>',
                                 '<title>{{title}}</title>')])
    submit = SubmitField('Submit')    

class ModulsForm_gdc_ch2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('<ul><li>...</li></ul>',
                                 '<ul><li>...</li></ul>'),
                                ('<ol><li>...</li></ol>',
                                 '<ol><li>...</li></ol>'),
                                ('<p><li>...</li></p>',
                                 '<p><li>...</li></p>')])
    submit = SubmitField('Submit') 

class ModulsForm_gdc_ch2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('forward',
                                 'forward'),
                                ('url_for',
                                 'url_for'),
                                ('redirect',
                                 'redirect')])
    submit = SubmitField('Submit')   

class ModulsForm_gdc_ch2_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Jinja2 main objective is to facilitate the introduction of JavaScript code in our templates',
                                 'Jinja2 main objective is to facilitate the introduction of JavaScript code in our templates'),
                                ('Jinja2 aims the introduction of CSS code in our templates',
                                 'Jinja2 aims the introduction of CSS code in our templates'),
                                ('Jinja2 is the Flask template engine that allows us to render variables and logical statements in our html files',
                                 'Jinja2 is the Flask template engine that allows us to render variables and logical statements in our html files')])
    submit = SubmitField('Submit')   

class ModulsForm_gdc_ch2_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('{% block content %} {% endblock %}',
                                 '{% block content %} {% endblock %}'),
                                ('{% extends %} {% extends %}',
                                 '{% extends %} {% extends %}'),
                                ('{% if statement %} {% endif statement %}',
                                 '{% if statement %} {% endif statement %}')])
    submit = SubmitField('Submit')           
