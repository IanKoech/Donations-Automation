from flask import redirect,render_template,request, url_for, flash
from . import auth
from ..models import Donor,Charity,clearusers
from .forms import Login
from flask_login import login_user, logout_user,login_required



@auth.route('/login/<role>', methods = ['GET', 'POST'])
def login(role):
    
    form = Login()
    if form.validate_on_submit():
        if role == 'Donor':
            user = Donor.query.filter_by(email = form.email.data).first()
            if user is not None and user.password == form.password.data:
                login_user(user,form.remember.data)
                return redirect(request.args.get('next') or url_for('donor.displaycharities'))

            flash('Invalid username or password')

        else:
            user = Charity.query.filter_by(email = form.email.data).first()
            if user is not None and user.password == form.password.data:

                login_user(user,form.remember.data)
                return redirect(request.args.get('next') or url_for('charity.charityprofile', user =user))

            flash('Invalid username or password')        

    
    return render_template('login.html', form =form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("donor.displaycharities"))