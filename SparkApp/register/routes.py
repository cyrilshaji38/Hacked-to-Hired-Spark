from flask import render_template, redirect, url_for, flash
from SparkApp.register.forms import SignupForm
from SparkApp.register.models import User
from SparkApp import app, db
from flask_login import login_user


@app.route("/register",methods = ['GET','POST'])
def register_page():
    form2 = SignupForm()
    if form2.validate_on_submit():
        user_to_create = User(username=form2.username.data,email=form2.email.data,mobile=form2.mobile.data,epassword=form2.password.data,acctype=form2.acctype.data)   
        db.session.add(user_to_create)   # Adds new user to database.
        db.session.commit()
        login_user(user_to_create)
        return redirect(url_for('test_page'))   # Redirect user to page with a sample test paper.
    if form2.errors != {}:
        for err_msg in form2.errors.values():
            flash(f'{err_msg}',category='danger')
    return render_template('register/register.html',form=form2)   