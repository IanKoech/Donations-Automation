from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TextAreaField,SubmitField,IntegerField,PasswordField
from wtforms.validators import Required, Email,EqualTo

class applicationform(FlaskForm):

    name = StringField('Name:', validators=[Required()])
    toDoList = TextAreaField('To Do List', validators=[Required()])
    phone_number = IntegerField('Phone Number:', validators=[Required()])
    email = StringField('Email:', validators=[Required(), Email()])
    Address = StringField('Address', validators=[Required()])
    preferedpassword = PasswordField('Prefered password', validators=[Required(), EqualTo('confirm_password','Passwords must match')])
    confirm_password = PasswordField('Confirm password', validators=[Required()])

    submit = SubmitField('Apply')

class BeneficiaryForm(FlaskForm):

    name = StringField('Name', validators=[Required()])
    inventory = IntegerField('Inventory:')
    stories = TextAreaField('User Story:')
    submit = SubmitField('Add Beneficiary')









