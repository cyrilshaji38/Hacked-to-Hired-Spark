from flask import render_template, url_for
from SparkApp import app
from flask_login import current_user


@app.route("/teacher")
def teacher_page():
    profile = url_for('static', filename='profile_pics/' + current_user.profile)
    return render_template('dashboard/teacher/teacher.html', profile=profile)