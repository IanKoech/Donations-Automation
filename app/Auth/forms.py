from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, SubmitField,BooleanField,IntegerField, PasswordField
from wtforms.validators import Required,Email,EqualTo


class Login(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    Role = SelectField('Role',choices=['Donor', 'Charity'], validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('login')


    



