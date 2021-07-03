from flask import render_template
from SparkApp import app


@app.route("/teacher")
def teacher_page():
    return render_template('dashboard/teacher/teacher.html')