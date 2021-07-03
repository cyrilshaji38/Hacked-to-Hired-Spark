from flask import render_template
from SparkApp import app


@app.route("/student")
def student_page():
    return render_template('dashboard/student/student.html')