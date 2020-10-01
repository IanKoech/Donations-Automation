from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

class Charity(db.Model):

    __tablename__ = 'charity'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    toDoList = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    email = db.Column(db.String)
    Address = db.Column(db.String)
    donationsReceived = db.Column(db.Integer)
    Beneficiaries = db.relationship('Beneficiaries', backref = 'charity', lazy = 'dynamic')
    accountDetails = db.Column(db.Integer)
   

    def save_charity(self):
        db.session.add(self)
        db.session.commit()


    

class Beneficiaries(db.Model):

    __tablename__ = 'beneficiaries'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    inventory = db.Column(db.Integer)
    stories = db.Column(db.String)
    Charity = db.Column(db.Integer, db.ForeignKey('charity.id'))

    def save_beneficiary(self):
        db.session.add(self)
        db.session.commit()


class Donor(db.Model):

    __tablename__ = 'donors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    accountdetails = db.Column(db.Integer)
    donation_frequency = db.Column(db.Boolean)
    reminding_time = db.Column(db.DateTime,default =datetime.utcnow)

    def save_donor(self):
        db.session.add(self)
        db.session.commit()



class Donations(db.Model):

    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key = True)
    donor = db.Column(db.String)
    donorAnonimity = db.Column(db.Boolean)
    Donee = db.Column(db.String)
    Amount = db.Column(db.Integer)
    Date = db.Column(db.DateTime, default = datetime.utcnow)

    def save_donation(self):
        db.session.add(self)
        db.session.commit()




def clearusers():
    Charity.query.delete()
    Donor.query.delete()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()



    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))





