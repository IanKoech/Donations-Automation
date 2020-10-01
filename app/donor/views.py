from flask import redirect, render_template, url_for
from .. import db
from ..models import Donations, Donor, Charity,Beneficiaries, User
from . import donor
from .forms import Create_Account, Donation_Form
from datetime import datetime
from ..email import reminder_message
from flask_login import login_required



@donor.route('/display/charities')
@login_required
def displaycharities():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    

    return render_template('charity/allcharities.html', charities = Allcharities, Donors = AllDonors)


@donor.route('/Donor/Create/account', methods =['GET', 'POST'])
def create_account():

    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()


    form = Create_Account()
    if form.validate_on_submit():
        name = form.name.data
        accountdetails  = form.account.data
        donation_frequency = form.donation_frequency.data
        email = form.email.data
        password = form.Prefered_password.data

        new_donor = Donor(name = name,accountdetails = accountdetails , donation_frequency = donation_frequency, email =email, password = password)
        user = User(username = name, email =email, password = password )
        new_donor.save_donor()
        user.save_user()

        return render_template('donor/donoraccountcreation.html', form = form, charities = Allcharities, Donors = AllDonors)

    return render_template('donor/donoraccountcreation.html', form = form, charities = Allcharities, Donors = AllDonors)


@donor.route('/Donor/Donate', methods = ['GET', 'POST'])
@login_required
def donate():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    form = Donation_Form()
    
    if form.validate_on_submit():

        donee = 'Dancan Sandys'
        donor = 'Dancan Oruko'
        amount = form.amount.data
        donorAnonymity = form.Anonymity.data

        new_donation = Donations(Donee= donee, donor = donor, Amount= amount)
        new_donation.save_donation()


        return render_template('donor/donoraccountcreation.html', form = form, charities = Allcharities, Donors = AllDonors)

    return render_template('donor/donoraccountcreation.html', form = form, charities = Allcharities, Donors = AllDonors)



@donor.route('/Remind/Donors')
@login_required
def remind():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    Donors = Donor.query.all()
    for Donor in Donors:
        if Donor.reminding_time == datetime.utcnow:
            reminder_message('A reminder for your monthly donations', 'reminder', Donor, **kwargs )

    return reminder_message('charity/allcharities.html', charities = Allcharities, Donors = AllDonors)            



@donor.route('/about/us')
def about():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    return render_template('about.html', charities = Allcharities, Donors = AllDonors)


@donor.route('/applying')
def applying():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    return render_template('applying.html', charities = Allcharities, Donors = AllDonors)

@donor.route('/')

def index():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    return render_template('index.html', charities = Allcharities, Donors = AllDonors)



