from flask import redirect,render_template,request, url_for, flash
from . import auth
from ..models import Donor,Charity,clearusers, User
from .forms import Login
from flask_login import login_user, logout_user,login_required
from flask_login import login_required





@auth.route('/login', methods = ['GET', 'POST'])
def login():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()


    
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.password == form.password.data:
            
            login_user(user,form.remember.data)      

            return redirect(request.args.get('next') or url_for('donor.index'))

        flash('Invalid username or Password')       

    
    return render_template('login.html', form =form, charities = Allcharities, Donors = AllDonors)

@auth.route('/logout')
@login_required
def logout():
    Allcharities = Charity.query.all()
    AllDonors = Charity.query.all()

    logout_user()
    return redirect(url_for("donor.displaycharities", charities = Allcharities, Donors = AllDonors))