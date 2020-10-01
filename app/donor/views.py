from flask import redirect, render_template, url_for
from .. import db
from ..models import Donations, Donor, Charity,Beneficiaries
from . import donor
from .forms import Create_Account, Donation_Form
from datetime import datetime
from ..email import reminder_message

@donor.route('/')
def displaycharities():

    charities = Charity.query.all()

    return render_template('/charity/allcharities.html', charities = charities)


@donor.route('/Donor/Create/account', methods =['GET', 'POST'])
def create_account():


    form = Create_Account()
    if form.validate_on_submit():
        name = form.name.data
        accountdetails  = form.account.data
        donation_frequency = form.donation_frequency.data

        new_donor = Donor(name = name,accountdetails = accountdetails , donation_frequency = donation_frequency)
        new_donor.save_donor()

        return render_template('donor/donoraccountcreation.html', form = form)

    return render_template('donor/donoraccountcreation.html', form = form)


@donor.route('/Donor/Donate', methods = ['GET', 'POST'])
def donate():


    form = Donation_Form()
    
    if form.validate_on_submit():

        donee = 'Dancan Sandys'
        donor = 'Dancan Oruko'
        amount = form.amount.data
        donorAnonymity = form.Anonymity.data

        new_donation = Donations(Donee= donee, donor = donor, Amount= amount)
        new_donation.save_donation()


        return render_template('donor/donoraccountcreation.html', form = form)

    return render_template('donor/donoraccountcreation.html', form = form)



@donor.route('/Remind/Donors')
def remind():
    Donors = Donor.query.all()
    for Donor in Donors:
        if Donor.reminding_time == datetime.utcnow:
            reminder_message('A reminder for your monthly donations', 'reminder', Donor, **kwargs )

    return reminder_message('charity/allcharities.html')            











