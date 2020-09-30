from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField, IntegerField
from wtforms.validators import Required, Email

class Create_Account(FlaskForm):
    
    name = StringField('Name:', validators=[Required()])
    anonymity = BooleanField('Do you want to be Anonymous?')
    account = IntegerField('Account Number:', validators=[Required()])
    donation_frequency =BooleanField('Autodonate monthly' )
    submit = SubmitField('Create Account')
    
class Donation_Form(FlaskForm):
    amount = IntegerField('Amount:')
    Anonymity = BooleanField('Do you want do donate anonymously')
    submit = SubmitField('Donate')

