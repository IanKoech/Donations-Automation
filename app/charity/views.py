from flask import render_template, redirect, url_for
from .. import db
from . import charity
from ..models import Charity
from .forms import applicationform

@charity.route('/charity/application', methods =['GET','POST'])
def apply():

    form = applicationform()
    if form.validate_on_submit():
        name = form.name.data
        toDoList = form.toDoList.data
        phoneNumber = form.phone_number.data
        email = form.email.data
        Address = form.Address.data

        new_charity = Charity(name = name, toDoList = toDoList, phoneNumber =phoneNumber, email =email, Address = Address)
        
        new_charity.save_charity()
        
        return render_template('charity/application.html', form = form)
    
    return render_template('charity/application.html', form = form)



    














