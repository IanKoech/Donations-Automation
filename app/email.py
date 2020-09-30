from flask_mail import Message
from flask import render_template
from . import mail

def reminder_message(Subject, template, to, **kwargs):
    sender_email = 'dancan.oruko99@gmail.com'

    email = Message(Subject, sender= sender_email, recipients=[to],)
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    mail.send(email)






