from SparkApp.dashboard.student.routes import student_page
from flask import render_template, redirect, url_for, flash
from SparkApp.login.forms import SigninForm
from SparkApp.register.models import User
from SparkApp import app
from flask_login import login_user, logout_user


@app.route("/",methods = ['GET','POST'])
def login_page():
    form1 = SigninForm()
    if form1.validate_on_submit():
        attempted_user = User.query.filter_by(username=form1.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form1.password.data):   # To ensure username and password match according to database.
            login_user(attempted_user)
            if(attempted_user.acctype == 1):
                return redirect(url_for('teacher_page'))
            else:
                return redirect(url_for('student_page'))
        else:
            flash('Username and password do not match! Please try again', category='danger')
    return render_template('login/login.html', form=form1)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login_page'))