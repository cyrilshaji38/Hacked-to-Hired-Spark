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
        my_students = Students.query.filter_by(teacher=current_user.id) 
        profile = url_for('static', filename='profile_pics/' + current_user.profile)
        form4 = AddStudentForm()
        if form4.validate_on_submit():
            if User.query.filter_by(username=form4.username.data).first():
                if Students.query.filter_by(username=form4.username.data).first():
                    print("already assigned a teacher!")
                else:
                    student_to_add = Students(username=form4.username.data,teacher=current_user.id)
                    db.session.add(student_to_add)
                    db.session.commit()
            else:
                print("no such student")
        return render_template('dashboard/teacher/teacher.html', profile=profile, form=form4, my_students=my_students)
    else:
        return redirect(url_for('login_page'))