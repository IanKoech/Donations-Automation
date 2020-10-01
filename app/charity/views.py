from flask import render_template, redirect, url_for
from .. import db
from . import charity
from ..models import Charity,Donations,Donor, Beneficiaries,User
from .forms import applicationform,BeneficiaryForm
from flask_login import login_required




@charity.route('/charity/application', methods =['GET','POST'])
def apply():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    form = applicationform()
    if form.validate_on_submit():
        name = form.name.data
        toDoList = form.toDoList.data
        phoneNumber = form.phone_number.data
        email = form.email.data
        Address = form.Address.data
        password = form.preferedpassword.data

        Role = 'Charity'

        new_charity = Charity(name = name, toDoList = toDoList, phoneNumber =phoneNumber, email =email, Address = Address, password= password)
        user = User(username = name, email =email, password = password,Role =Role )
        new_charity.save_charity()
        user.save_user()
        
        return redirect(url_for('auth.login', charities = Allcharities, Donors = AllDonors))
    
    return render_template('charity/application.html', form = form)

@charity.route('/charity/profile/<charityname>', methods = ['GET', 'POST'])
@login_required
def charityprofile(charityname):
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()
    charity = Charity.query.filter_by(name = charityname ).first()
    donations_recieved = Donations.query.filter_by(Donee = charityname ).all()

    total_donations = 0

    for donation in donations_recieved:
        total_donations = total_donations + donation.Amount
    

    return render_template('/charity/charityprofile.html', donations = donations_recieved, total_donations = total_donations, charities = Allcharities, Donors = AllDonors)

@charity.route('/charity/beneficiaries/update/<charityname>', methods = ['GET', 'POST'])
@login_required
def addbeneficiaries(charityname):
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()
    form = BeneficiaryForm()
    if form.validate_on_submit():
        charity = charityname
        name = form.name.data
        inventory = form.inventory.data
        stories = form.stories.data

        new_beneficiary = Beneficiaries(name = name, inventory= inventory, stories = stories,Charity = charity)
        new_beneficiary.save_beneficiary()

        return render_template('charity/addbeneficiary.html', form =form)

    return render_template('charity/addbeneficiary.html' , form =form)

@charity.route('/charity/beneficiaries/<charityname>', methods = ['GET', 'POST'])
@login_required
def currentbeneficiaries(charityname): 
    

    Currentbeneficiaries = Beneficiaries.query.filter_by(Charity = charityname) 
    
    return render_template('charity/beneficiaries.html', beneficiaries = Currentbeneficiaries)














