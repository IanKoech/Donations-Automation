from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TextAreaField,SubmitField,IntegerField
from wtforms.validators import Required, Email

class applicationform(FlaskForm):

    name = StringField('Name:', validators=[Required()])
    toDoList = TextAreaField('To Do List', validators=[Required()])
    phone_number = IntegerField('Phone Number:', validators=[Required()])
    email = StringField('Email:', validators=[Required(), Email()])
    Address = StringField('Address', validators=[Required()])
    submit = SubmitField('Apply')










