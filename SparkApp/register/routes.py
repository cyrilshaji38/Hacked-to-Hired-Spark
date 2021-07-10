from flask import render_template, redirect, url_for, flash
from SparkApp.register.forms import SignupForm
from SparkApp.register.models import User
from SparkApp import app, db
from flask_login import login_user, current_user
import secrets, os
from PIL import Image


@app.route("/register",methods = ['GET','POST'])
def register_page():
    form2 = SignupForm()   # Register form.
    if form2.validate_on_submit():
        if form2.profile.data:
            picture_file = save_picture(form2.profile.data)   # Profile picture uploaded by user.
        else:
            picture_file = form2.profile.data   # Gives a default profile picture if user has not uploaded one.
        user_to_create = User(
            username=form2.username.data,
            email=form2.email.data,
            mobile=form2.mobile.data,
            profile=picture_file,
            epassword=form2.password.data,
            acctype=form2.acctype.data
            )
        db.session.add(user_to_create)   # Adds new user to table 'User' in database.
        db.session.commit()
        login_user(user_to_create)
        if(user_to_create.acctype == 1):
            return redirect(url_for('teacher_page'))   # Redirect to teacher dashboard.
        else:
            return redirect(url_for('student_page'))   # Redirect to student dashboard.
    if form2.errors != {}:   # Validation errors from the register form.
        for err_msg in form2.errors.values():
            flash(f'{err_msg}',category='danger')
    return render_template('register/register.html',form=form2) 


def save_picture(form_picture):   # Converts and saves uploaded profile picture into static folder.
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn  