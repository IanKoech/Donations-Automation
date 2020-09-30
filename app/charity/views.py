from flask import render_template, redirect, url_for
from .. import db
from . import charity
from ..models import Charity,Donations,Donor, Beneficiaries
from .forms import applicationform,BeneficiaryForm

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

@charity.route('/charity/profile', methods = ['GET', 'POST'])
def charityprofile():
    charity = Charity.query.filter_by(name = 'Dancan Sandys' ).first()
    donations_recieved = Donations.query.filter_by(Donee = 'Dancan Sandys' ).all()

    total_donations = 0

    for donation in donations_recieved:
        total_donations = total_donations + donation.Amount
    

    return render_template('/charity/charityprofile.html', donations = donations_recieved, total_donations = total_donations)

@charity.route('/charity/beneficiaries/update', methods = ['GET', 'POST'])
def addbeneficiaries():
    form = BeneficiaryForm()
    if form.validate_on_submit():
        name = form.name.data
        inventory = form.inventory.data
        stories = form.stories.data

        new_beneficiary = Beneficiaries(name = name, inventory= inventory, stories = stories)
        new_beneficiary.save_beneficiary()

        return render_template('charity/addbeneficiary.html', form =form)

    return render_template('charity/addbeneficiary.html' , form =form)
    


    














