from flask import render_template, redirect, url_for, flash
from SparkApp.login.forms import SigninForm
from SparkApp.register.models import User
from SparkApp import app
from flask_login import login_user


@app.route("/",methods = ['GET','POST'])
def login_page():
    form1 = SigninForm()
    if form1.validate_on_submit():
        attempted_user = User.query.filter_by(username=form1.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form1.password.data):   # To ensure username and password match according to database.
            login_user(attempted_user)
            return redirect(url_for('test_page'))   # Redirect user to page with a sample test paper.
        else:
            flash('Username and password do not match! Please try again', category='danger')
    return render_template('login/login.html', form=form1)