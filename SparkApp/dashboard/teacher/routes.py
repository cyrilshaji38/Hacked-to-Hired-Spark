from flask import render_template, url_for
from werkzeug.utils import redirect
from SparkApp import app
from flask_login import current_user


@app.route("/teacher")
def teacher_page():
    if current_user.is_authenticated:
        profile = url_for('static', filename='profile_pics/' + current_user.profile)
        return render_template('dashboard/teacher/teacher.html', profile=profile)
    else:
        return redirect(url_for('login_page'))