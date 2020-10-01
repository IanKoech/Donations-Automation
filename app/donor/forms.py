from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField, IntegerField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class Create_Account(FlaskForm):
    
    name = StringField('Name:', validators=[Required()])
    account = IntegerField('Account Number:', validators=[Required()])
    donation_frequency =BooleanField('Autodonate monthly' )
    email = StringField('Email:',validators=[Required(), Email()])
    Prefered_password = PasswordField('Prefered password:', validators=[Required(),EqualTo('confirm_password', 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Create Account')
    
class Donation_Form(FlaskForm):
    amount = IntegerField('Amount:')
    Anonymity = BooleanField('Do you want do donate anonymously')
    submit = SubmitField('Donate')

