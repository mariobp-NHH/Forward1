from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField,  SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange 
from webse.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username', 
                         validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password',
                      validators=[DataRequired(), EqualTo('password')])                                
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
      user = User.query.filter_by(email=email.data).first()
      if user:
          raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login') 

# Bus form
class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')])
  submit = SubmitField('Submit')

# Car form ("standard" car)
class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of fuel', [InputRequired()], 
    choices=[('Gasoline', 'Gasoline'),
             ('Diesel', 'Diesel'),
             ('Hybrid', 'Hybrid'),
             ('Electric', 'Electric'),
             ('Hydrogen', 'Hydrogen')])
  submit = SubmitField('Submit')

# Car form (connected to API)
class SpecificCarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  model = StringField("Model", [InputRequired()])
  submit = SubmitField('Submit')

# Plane form
class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of flight and class', [InputRequired()], 
    choices=[('Short-haul (Buisness)','Short-haul (Buisness)'),
             ('Long-haul (Economy)','Long-haul (Economy)'),
             ('Long-haul (Premium economy)', 'Long-haul (Premium economy)'),
             ('Long-haul (First-class)','Long-haul (First-class)'),
             ('International (Economy)', 'International (Economy)'),
             ('International (Premium economy)','International (Premium economy)'), 
             ('International (Buisness)', 'International (Buisness)'),
             ('International (First Class)','International (First Class)')])
  submit = SubmitField('Submit')

# Ferry form
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of ferry', [InputRequired()], 
    choices=[('Regular', 'Regular'),
             ('High-speed', 'High-speed')])
  submit = SubmitField('Submit')  

# Train form
class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'),
             ('Electric (Nordic)', 'Electric (Nordic)'),
             ('Electric (EU)', 'Electric (EU)')])
  submit = SubmitField('Submit')  

# Motorbike form
class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Engine size', [InputRequired()], 
    choices=[('≤125cc', '≤125cc'), ('125cc to 500cc', '125cc to 500cc'),('>500cc','>500cc')])
  submit = SubmitField('Submit')

# Bike form
class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

# Walk form
class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  
