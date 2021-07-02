from flask import render_template
from SparkApp import app


@app.route("/communication")
def communication_page():
    return render_template('skills/communication.html')


@app.route("/critical_thinking")
def critical_thinking_page():
    return render_template('skills/critical_thinking.html')