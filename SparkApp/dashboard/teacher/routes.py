from flask.helpers import flash
from SparkApp.register.models import Students
from SparkApp.dashboard.teacher.forms import AddStudentForm
from flask import render_template, url_for
from werkzeug.utils import redirect
from SparkApp import app, db
from flask_login import current_user
from SparkApp.register.models import User


@app.route("/teacher", methods=['GET','POST'])
def teacher_page():
    if current_user.is_authenticated:
        my_students = Students.query.filter_by(teacher=current_user.id)   # Students assigned to current user's account.
        profile = url_for('static', filename='profile_pics/' + current_user.profile)   # Profile picture pulled from database.
        form4 = AddStudentForm()
        if form4.validate_on_submit():
            if User.query.filter_by(username=form4.username.data).first():   # Checks if entered student exists in User table.
                if Students.query.filter_by(username=form4.username.data).first():   # Checks if entered student is already assigned to a teacher.
                    flash("Student already assigned to a teacher!", category='danger')
                else:
                    student_to_add = Students(username=form4.username.data,teacher=current_user.id)   # Adds student to Student table and assigns a teacher.
                    db.session.add(student_to_add)
                    db.session.commit()
            else:
                flash("No such student!", category='danger')
        return render_template('dashboard/teacher/teacher.html', profile=profile, form=form4, my_students=my_students)
    else:
        return redirect(url_for('login_page'))