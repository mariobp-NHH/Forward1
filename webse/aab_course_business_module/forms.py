from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional
from webse.models import User

class ModulsForm_m2_ch1_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Reducing the waste of food in supermarkets and restaurants', 'Reducing the waste of food in supermarkets and restaurants'),
                                ('Reducing transport carbon emissions and the public transport', 'Reducing transport carbon emissions and the public transport'),
                                ('Improving the recycling system', 'Improving the recycling system')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch1_e3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch1_e4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The reduction in methane emissions', 'The reduction in methane emissions'),
                                ('The reduction of plastic in the nature', 'The reduction of plastic in the nature'),
                                ('The recycling of residues', 'The recycling of residues')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Heating in buildings', 'Heating in buildings'),
                                ('Incineration, and gasification to obtain biodiesel and hydrogen', 'Incineration, and gasification to obtain biodiesel and hydrogen'),
                                ('Compost to be used in agriculture', 'Compost to be used in agriculture')])
    submit = SubmitField('Submit')   
