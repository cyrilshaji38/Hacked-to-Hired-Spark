from flask import render_template, url_for
from werkzeug.utils import redirect
from SparkApp import app
from flask_login import current_user


@app.route("/student")
def student_page():
    if current_user.is_authenticated:
        profile = url_for('static', filename='profile_pics/' + current_user.profile)   # Profile picture pulled from database.
        return render_template('dashboard/student/student.html', profile=profile)   # Student dashboard.
    else:
        return redirect(url_for('login_page'))