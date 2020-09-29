from . import db
from datetime import datetime

class Charity(db.Model):

    __tablename__ = 'charity'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    toDoList = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    email = db.Column(db.String)
    Address = db.Column(db.String)
    donationsReceived = db.Column(db.Integer)
    Beneficiaries = db.relationship('Beneficiaries', backref = 'Charity', lazy = 'dynamic')
    accountDetails = db.Column(db.Integer)

class Beneficiaries(db.Model):

    __tablename__ = 'beneficiaries'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    inventory = db.Column(db.Integer)
    stories = db.Column(db.String)
    Charity = db.Column(db.Integer, db.ForeignKey('charity.id'))

class Donor(db.Model):

    __tablename__ = 'donors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    anonymity = db.Column(db.Boolean)
    accountdetails = db.Column(db.Integer)
    charities = db.Column(db.String)
    donation_frequency = db.Column(db.Boolean)
    reminding_time = db.Column(db.DateTime,default =datetime.utcnow)

class Donations(db.Model):

    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key = True)
    donor = db.Column(db.String)
    Donee = db.Column(db.String)
    Amount = db.Column(db.Integer)
    Date = db.Column(db.DateTime, default = datetime.utcnow)















